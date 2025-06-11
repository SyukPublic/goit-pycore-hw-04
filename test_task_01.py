# -*- coding: utf-8 -*-"

"""
Tests for task 01
"""

from pathlib import Path

from tasks.task_01 import total_salary


def main() -> None:
    try:
        total, average = total_salary("salaries.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(e)

    try:
        total, average = total_salary("./data/salaries.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(e)

    try:
        total, average = total_salary(Path.cwd() / "./data/salaries.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()