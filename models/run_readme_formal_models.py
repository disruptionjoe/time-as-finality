"""Run formal-model modules declared by the README."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Mapping, Sequence, TextIO


README_HEADING = "## Run The Formal Model"
SELF_MODULE = "models.run_readme_formal_models"
README_MODULE_RE = re.compile(r"^python\s+-m\s+(models\.[A-Za-z0-9_.]+)\s*$")


@dataclass(frozen=True)
class ModuleRun:
    module: str
    command: tuple[str, ...]
    returncode: int


@dataclass(frozen=True)
class RunnerReport:
    modules: tuple[str, ...]
    runs: tuple[ModuleRun, ...]
    returncode: int


Runner = Callable[..., object]


def configure_stdio_utf8() -> None:
    """Keep this wrapper's own output Unicode-safe where Python supports it."""

    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="replace")


def utf8_child_env(base_env: Mapping[str, str] | None = None) -> dict[str, str]:
    env = dict(os.environ if base_env is None else base_env)
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    return env


def extract_readme_formal_model_modules(readme_text: str) -> tuple[str, ...]:
    modules: list[str] = []
    in_section = False
    in_fence = False

    for raw_line in readme_text.splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            if in_section and line != README_HEADING:
                break
            in_section = line == README_HEADING
            in_fence = False
            continue

        if not in_section:
            continue

        if line.startswith("```"):
            in_fence = not in_fence
            continue

        if not in_fence:
            continue

        match = README_MODULE_RE.match(line)
        if match:
            module = match.group(1)
            if module != SELF_MODULE:
                modules.append(module)

    if not modules:
        raise ValueError(f"no formal model modules found under {README_HEADING!r}")

    return tuple(modules)


def read_readme_formal_model_modules(readme_path: Path = Path("README.md")) -> tuple[str, ...]:
    return extract_readme_formal_model_modules(readme_path.read_text(encoding="utf-8"))


def _matches_start_after(candidate: str, start_after: str) -> bool:
    return start_after in {
        candidate,
        candidate.rsplit(".", 1)[-1],
        f"python -m {candidate}",
    }


def select_modules_after(
    modules: Iterable[str],
    start_after: str | None = None,
) -> tuple[str, ...]:
    selected = tuple(modules)
    if start_after is None:
        return selected

    for index, module in enumerate(selected):
        if _matches_start_after(module, start_after):
            return selected[index + 1 :]

    raise ValueError(f"start-after target not found in README runner list: {start_after}")


def command_for_module(module: str, python_executable: str | None = None) -> tuple[str, ...]:
    return (python_executable or sys.executable, "-m", module)


def display_command(module: str) -> str:
    return f"python -m {module}"


def run_modules(
    modules: Sequence[str],
    *,
    runner: Runner = subprocess.run,
    python_executable: str | None = None,
    base_env: Mapping[str, str] | None = None,
    dry_run: bool = False,
    stdout: TextIO | None = None,
) -> RunnerReport:
    stream = stdout or sys.stdout
    env = utf8_child_env(base_env)
    runs: list[ModuleRun] = []

    for module in modules:
        command = command_for_module(module, python_executable)
        if dry_run:
            print(display_command(module), file=stream)
            runs.append(ModuleRun(module=module, command=command, returncode=0))
            continue

        print(f"==> {display_command(module)}", file=stream, flush=True)
        completed = runner(command, env=env, check=False)
        returncode = int(getattr(completed, "returncode"))
        runs.append(ModuleRun(module=module, command=command, returncode=returncode))

        if returncode != 0:
            print(
                f"Stopped after {display_command(module)} failed with exit code {returncode}.",
                file=stream,
                flush=True,
            )
            return RunnerReport(modules=tuple(modules), runs=tuple(runs), returncode=returncode)

    return RunnerReport(modules=tuple(modules), runs=tuple(runs), returncode=0)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run README-declared formal-model runner modules in order."
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=Path("README.md"),
        help="README path to read runner declarations from.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Print declared module names without running them.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print runner commands without executing them.",
    )
    parser.add_argument(
        "--start-after",
        help="Resume with the module after this full module name, basename, or README command.",
    )
    return parser


def main(
    argv: Sequence[str] | None = None,
    *,
    runner: Runner = subprocess.run,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    configure_stdio_utf8()
    parser = _build_parser()
    args = parser.parse_args(argv)
    out = stdout or sys.stdout
    err = stderr or sys.stderr

    try:
        modules = read_readme_formal_model_modules(args.readme)
        selected = select_modules_after(modules, args.start_after)
    except OSError as exc:
        print(f"error: {exc}", file=err)
        return 2
    except ValueError as exc:
        print(f"error: {exc}", file=err)
        return 2

    if args.list:
        for module in selected:
            print(module, file=out)
        return 0

    report = run_modules(selected, runner=runner, dry_run=args.dry_run, stdout=out)
    return report.returncode


if __name__ == "__main__":
    raise SystemExit(main())
