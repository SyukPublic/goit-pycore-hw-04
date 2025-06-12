# -*- coding: utf-8 -*-"

"""
Core functions for task 03
"""

from typing import Any, Union
from pathlib import Path
from colorama import Fore

from .cutil import print_colored
from .futil import get_absolute_path, build_directory_tree


def get_directory_tree(directory_path: Union[Path, str]) -> dict[str, Any]:
    """Get the directory tree

    :param directory_path: specified directory path (str, Path, mandatory)
    :return: Directory tree (dict)
    """

    # Determining the absolute directory path
    directory_path = get_absolute_path(directory_path, current_dir=Path.cwd())

    # Build and return the directory tree
    return build_directory_tree(directory_path)

def print_directory_info(
        directory_info: dict[str, Any],
        level: int = 0,
        indent : str = "    ",
        sort: bool = False,
        directories_first: bool = False,
) -> None:
    """Print of the directory contents

    :param directory_info: directory info (dictionary, mandatory)
    :param level :  level for pretty-printed with that indent level (int, optional)
    :param indent : indent for pretty-printed with that indent level (string, optional)
    :param sort : sort the directory objects in alphabetical order (boolean, optional)
    :param directories_first : print directories before files (boolean, optional)
    :return: None value
    """

    print_colored(Fore.BLUE, "{indent}{name}/".format(indent=indent * level, name=directory_info.get("name", "")))

    # Get the children and sort them if specified
    directory_children: list[dict[str, Any]] = directory_info.get("children", [])
    if sort:
        directory_children = sorted(
            directory_children,
            key=lambda i: ((i.get("type", "") if directories_first else "") + i.get("name", "")).lower()
        )

    # Print the children
    for child_info in directory_children:
        if child_info.get("type") == "directory":
            # For the directory type object, print the next level info
            print_directory_info(
                child_info,
                level=level + 1,
                indent=indent,
                sort=sort,
                directories_first=directories_first,
            )
        else:
            # For the file type object, print name
            print_colored(
                Fore.GREEN,
                "{indent}{name}".format(indent=indent * (level + 1), name=child_info.get("name", ""))
            )


def print_directory_tree(directory_path: Union[Path, str], sort: bool = False, directories_first: bool = False) -> None:
    """Print to the console directory tree

    :param directory_path: specified directory path (str, Path, mandatory)
    :param sort : sort the directory objects in alphabetical order (boolean, optional)
    :param directories_first : print directories before files (boolean, optional)
    :return: None value
    """

    print_directory_info(get_directory_tree(directory_path), sort=sort, directories_first=directories_first)