# -*- coding: utf-8 -*-"

"""
Tests for task 02
"""

from pathlib import Path

from tasks.task_02 import get_cats_info


def main() -> None:
    try:
        # Test the relative path to the file
        print(get_cats_info("./data/cats_file.txt"))
    except Exception as e:
        print(e)

    try:
        # Test the absolute path to the file
        print(get_cats_info(Path.cwd() / "./data/cats_file.txt"))
    except Exception as e:
        print(e)

    try:
        # Test the wrong path to the file
        print(get_cats_info("cats_file.txt"))
    except Exception as e:
        print(e)

    try:
        # Test the path to the directory
        print(get_cats_info("./data"))
    except Exception as e:
        print(e)

    try:
        # Test the binary data file
        print(get_cats_info("./data/bindata.dat"))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()