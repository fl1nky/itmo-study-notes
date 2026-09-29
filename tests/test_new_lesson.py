from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

from tools import new_lesson


class NewLessonTests(unittest.TestCase):
    def test_creates_dated_folder_and_index(self) -> None:
        with tempfile.TemporaryDirectory() as temp, patch.object(new_lesson, "ROOT", Path(temp)):
            course = Path(temp) / "дисциплины" / "dm"
            course.mkdir(parents=True)
            (course / "README.md").write_text(
                "# Дискретная математика\n<!-- LESSONS:START -->\nПока занятий нет.\n<!-- LESSONS:END -->\n",
                encoding="utf-8",
            )
            note = new_lesson.create_lesson("dm", date(2026, 9, 29), "Множества и операции", "лекция")
            self.assertEqual(note.parent.name, "2026-09-29 (Множества и операции)")
            self.assertIn("## Главы и вопросы", note.read_text(encoding="utf-8"))
            index = (course / "README.md").read_text(encoding="utf-8")
            self.assertIn("2026-09-29", index)
            self.assertIn("Множества и операции", index)
            with self.assertRaises(FileExistsError):
                new_lesson.create_lesson("dm", date(2026, 9, 29), "Множества и операции", "лекция")

    def test_rejects_invalid_windows_filename(self) -> None:
        with self.assertRaises(ValueError):
            new_lesson.safe_topic("Введение: множества")


if __name__ == "__main__":
    unittest.main()
