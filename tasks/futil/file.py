# -*- coding: utf-8 -*-"

"""
Functions for works with the files and directories
"""

import json
from typing import Optional, Any, Union
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

def load_text_file_data(file_path: Path, remove_empty_lines: bool = False) -> list[str]:
    """Return the content of the given text file

    :param file_path: specified text file path (Path, mandatory)
    :param remove_empty_lines: determines whether to remove empty lines (bool, optional)
    :return: file content (list of strings)
    """

    # Verify that the specified file exists
    if not file_path.exists():
        raise ValueError(f'The file "{file_path}" not found')

    # Verify that the specified path is the file
    if not file_path.is_file():
        raise ValueError(f'The specified path "{file_path}" is not a file')

    # Open the specified file as a text file
    try:
        with open(file_path, 'tr', encoding='utf-8') as fh:
            # Read the file data
            # file_content = [line for line in fh.readlines() if not remove_empty_lines or line.strip()]
            file_content = [line for line in fh if not remove_empty_lines or line.strip()]
            # Return the file data
            return file_content
    except UnicodeDecodeError:
        # The file data is corrupted
        # Raise exception to the upper level
        raise ValueError(f'The file "{file_path}" data is corrupted')
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))


def load_json_file_data(
        file_path: Path,
        ignore_if_not_exist: bool = False,
) -> Optional[Union[dict[str, Any], list[Any]]]:
    """Deserialize and return the content of the given JSON file

    :param file_path: specified text file path (Path, mandatory)
    :param ignore_if_not_exist: return None if the file does not exist (bool, optional)
    :return: deserialized JSON (dictionary, list, optional)
    """

    # Verify that the specified file exists
    if not file_path.exists():
        if ignore_if_not_exist:
            return None
        raise ValueError(f'The file "{file_path}" not found')

    # Verify that the specified path is the file
    if not file_path.is_file():
        raise ValueError(f'The specified path "{file_path}" is not a file')

    # Read the file data and deserialize
    try:
        return json.loads(file_path.read_text(encoding='utf-8'), strict=False)
    except UnicodeDecodeError:
        # The file data is corrupted
        # Raise exception to the upper level
        raise ValueError(f'The file "{file_path}" data is corrupted')
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))


def write_json_file_data(file_path: Path, data: Union[dict[str, Any], list[Any]]) -> None:
    """Serialize and write the content to the given JSON file

    :param file_path: specified text file path (Path, mandatory)
    :param data: return None if the file does not exist (bool, mandatory)
    """

    # Verify that the specified path is the file if it already exists
    if file_path.exists() and not file_path.is_file():
        raise ValueError(f'The specified path "{file_path}" is not a file')

    # Make the data directory if it does not exist
    file_path.parent.mkdir(exist_ok=True)

    # Serialize data and write to the file
    try:
        file_path.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding='utf-8')
    except UnicodeEncodeError:
        # The file data is corrupted
        # Raise exception to the upper level
        raise ValueError(f'The data can not be encoded and written to a file')
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))


def build_directory_tree(directory_path: Path) -> dict[str, Any]:
    """Return the given directory tree with metadata

    :param directory_path: specified directory absolute path (Path, mandatory)
    :return: directory tree (dictionary)
    """

    # Verify that the specified path exists
    if not directory_path.exists():
        raise ValueError(f'The path "{directory_path}" not found')

    # Verify that the specified path is the file
    if not directory_path.is_dir():
        raise ValueError(f'The specified path "{directory_path}" is not a directory')

    dir_tree: dict[str, Any] = dict(
        name=directory_path.name,
        type='directory',
        stat=directory_path.stat(),
        children=[],
    )

    # Iterate of the directory contents
    for child in directory_path.iterdir():
        if child.is_dir():
            dir_tree['children'].append(build_directory_tree(child))
        else:
            dir_tree['children'].append(
                dict(
                    name=child.name,
                    type='file',
                    stat=child.stat(),
                )
            )

    return dir_tree
