"""Tests for the README-declared formal model runner."""

from __future__ import annotations

import io
import subprocess
import tempfile
import unittest
from pathlib import Path

from models.run_readme_formal_models import (
    extract_readme_formal_model_modules,
    main,
    read_readme_formal_model_modules,
    run_modules,
    select_modules_after,
    utf8_child_env,
)


README_FIXTURE = """# Project

## Other

```bash
python -m models.run_ignored
```

## Run The Formal Model

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python -m models.run_t1
python -m models.run_t2
python -m models.run_emergence_lab
```

## Run Explorations

```bash
python -m models.run_ts_persona_sprint
```
"""


class ReadmeFormalModelRunnerTests(unittest.TestCase):
    def test_extracts_only_formal_model_modules_in_readme_order(self) -> None:
        modules = extract_readme_formal_model_modules(README_FIXTURE)

        self.assertEqual(
            modules,
            (
                "models.run_t1",
                "models.run_t2",
                "models.run_emergence_lab",
            ),
        )

    def test_extract_rejects_missing_runner_section(self) -> None:
        with self.assertRaises(ValueError):
            extract_readme_formal_model_modules("# Project\n")

    def test_current_readme_module_list_has_expected_boundary(self) -> None:
        modules = read_readme_formal_model_modules(Path("README.md"))

        self.assertEqual(modules[0], "models.run_t1")
        self.assertIn("models.run_t56", modules)
        self.assertEqual(modules[-1], "models.run_t75")
        self.assertNotIn("models.run_ts_persona_sprint", modules)

    def test_start_after_accepts_full_module_name(self) -> None:
        selected = select_modules_after(
            ("models.run_t1", "models.run_t2", "models.run_t3"),
            "models.run_t1",
        )

        self.assertEqual(selected, ("models.run_t2", "models.run_t3"))

    def test_start_after_accepts_basename(self) -> None:
        selected = select_modules_after(
            ("models.run_t1", "models.run_t2", "models.run_t3"),
            "run_t2",
        )

        self.assertEqual(selected, ("models.run_t3",))

    def test_start_after_rejects_unknown_target(self) -> None:
        with self.assertRaises(ValueError):
            select_modules_after(("models.run_t1",), "models.run_missing")

    def test_utf8_child_env_overrides_text_encoding_settings(self) -> None:
        env = utf8_child_env({"PYTHONUTF8": "0", "PYTHONIOENCODING": "latin-1"})

        self.assertEqual(env["PYTHONUTF8"], "1")
        self.assertEqual(env["PYTHONIOENCODING"], "utf-8")

    def test_dry_run_prints_commands_without_invoking_runner(self) -> None:
        calls = []

        def fake_runner(*args, **kwargs):
            calls.append((args, kwargs))
            return subprocess.CompletedProcess(args[0], 0)

        out = io.StringIO()
        report = run_modules(
            ("models.run_t1", "models.run_t2"),
            runner=fake_runner,
            python_executable="py",
            dry_run=True,
            stdout=out,
        )

        self.assertEqual(calls, [])
        self.assertEqual(report.returncode, 0)
        self.assertEqual(
            out.getvalue().splitlines(),
            ["python -m models.run_t1", "python -m models.run_t2"],
        )

    def test_run_modules_passes_utf8_env_and_stops_on_failure(self) -> None:
        calls = []

        def fake_runner(command, **kwargs):
            calls.append((command, kwargs))
            returncode = 7 if command[-1] == "models.run_t2" else 0
            return subprocess.CompletedProcess(command, returncode)

        out = io.StringIO()
        report = run_modules(
            ("models.run_t1", "models.run_t2", "models.run_t3"),
            runner=fake_runner,
            python_executable="py",
            base_env={"PYTHONUTF8": "0"},
            stdout=out,
        )

        self.assertEqual(report.returncode, 7)
        self.assertEqual([run.module for run in report.runs], ["models.run_t1", "models.run_t2"])
        self.assertEqual([call[0] for call in calls], [("py", "-m", "models.run_t1"), ("py", "-m", "models.run_t2")])
        self.assertEqual(calls[0][1]["env"]["PYTHONUTF8"], "1")
        self.assertEqual(calls[0][1]["env"]["PYTHONIOENCODING"], "utf-8")
        self.assertFalse(calls[0][1]["check"])
        self.assertIn("Stopped after python -m models.run_t2 failed", out.getvalue())

    def test_main_list_uses_readme_file_and_start_after(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            readme = Path(tmpdir) / "README.md"
            readme.write_text(README_FIXTURE, encoding="utf-8")
            out = io.StringIO()

            code = main(
                ["--readme", str(readme), "--list", "--start-after", "run_t1"],
                stdout=out,
                stderr=io.StringIO(),
            )

        self.assertEqual(code, 0)
        self.assertEqual(
            out.getvalue().splitlines(),
            ["models.run_t2", "models.run_emergence_lab"],
        )

    def test_main_returns_two_for_unknown_start_after(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            readme = Path(tmpdir) / "README.md"
            readme.write_text(README_FIXTURE, encoding="utf-8")
            err = io.StringIO()

            code = main(
                ["--readme", str(readme), "--start-after", "models.run_missing"],
                stdout=io.StringIO(),
                stderr=err,
            )

        self.assertEqual(code, 2)
        self.assertIn("start-after target not found", err.getvalue())


if __name__ == "__main__":
    unittest.main()
