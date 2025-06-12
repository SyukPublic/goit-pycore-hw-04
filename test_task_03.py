# -*- coding: utf-8 -*-"

"""
Tests for task 03
"""

import sys
import colorama
from typing import Optional


from tasks.task_03 import print_directory_tree


def main() -> None:
    try:
        directory: Optional[str] = None

        # Check whether the script was run with a directory specified as an argument
        if len(sys.argv) > 1:
            # The script was run with at least one argument - copy first argument value to the directory path
            directory = sys.argv[1]
        else:
            # The script was run without arguments – prompt the user to enter the directory path via user input
            directory = input('Enter directory name: ')

        print_directory_tree(directory, sort=True, directories_first=True)
    except Exception as e:
        print(colorama.Fore.RED + str(e))

    # Reset console styles to default
    print(colorama.Style.RESET_ALL)


if __name__ == "__main__":
    main()
