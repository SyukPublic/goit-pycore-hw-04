# -*- coding: utf-8 -*-"

"""
Functions for works with files and directories
"""

from typing import Optional, Union
from pathlib import Path


def get_absolute_path(path: Union[Path, str], current_dir: Optional[Union[Path, str]] = None) -> Path:
    """Return the absolute path for the given path and the current directory

    :param path: specified path (str, Path, mandatory)
    :param current_dir: current directory (str, Path, optional)
    :return: absolute path (Path)
    """
    if not path:
        # The path can not be None or an empty string
        raise ValueError('The path can not be empty')

    if Path(path).is_absolute():
        # If the specified path is an absolute - return it
        return Path(path)

    if current_dir is not None and isinstance(current_dir, str):
        # If the current directory is not specified, use the current working directory
        current_dir = Path(current_dir)

    # Construct an absolute path and return
    return (current_dir if current_dir is not None else Path.cwd()) / path

def load_text_file_data(file_path: Path) -> list[str]:
    """Return the content of the given text file

    :param file_path: specified text file path (Path, mandatory)
    :return: file content (list of strings)
    """

    # Verify that the specified file exists
    if not file_path.exists():
        raise ValueError(f'The file "{file_path}" not found')

    # Verify that the specified file is the file
    if not file_path.is_file():
        raise ValueError(f'The specified path "{file_path}" is not a file')

    # Open the specified file as a text file
    with open(file_path, 'tr', encoding='utf-8') as fh:
        # Return the file content
        return fh.readlines()
