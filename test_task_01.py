# -*- coding: utf-8 -*-"

"""
Tests for task 01
"""

from pathlib import Path

from tasks.task_01 import total_salary


def main() -> None:
    try:
        # Test the relative path to the file
        total, average = total_salary("./tasks/data/salaries.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(e)

    try:
        # Test the absolute path to the file
        total, average = total_salary(Path.cwd() / "./tasks/data/salaries.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(e)

    try:
        # Test the wrong path to the file
        total, average = total_salary("salaries.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(e)

    try:
        # Test the path to the directory
        total, average = total_salary("./tasks/data")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(e)

    try:
        # Test the binary data file
        total, average = total_salary("tasks/data/bindata.dat")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()