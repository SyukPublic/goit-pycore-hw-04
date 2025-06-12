# -*- coding: utf-8 -*-"

"""
Core functions for task 02
"""

from typing import Union
from pathlib import Path

from .futil import get_absolute_path, load_text_file_data


def get_cats(cats_file: Union[Path, str]) -> list[dict[str, str]]:
    """Load cats from the given file and return info about unique cats

    :param cats_file: specified cats data file path (str, Path, mandatory)
    :return: cats data (list of dict)
    """

    # Load the cats data from the file, remove any empty lines, and prepare the information for further analysis
    try:
        cats_raw: list[tuple[str, ...]] = [
            tuple(data_row.strip().split(","))
            for data_row in load_text_file_data(get_absolute_path(cats_file), remove_empty_lines=True)
        ]
    except ValueError as e:
        # Exceptions handled by the previous level
        # Raise exception to the upper level
        raise e
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))

    try:
        # Set of unique cats id already added to the list of cats info
        cats_ids = set()

        # Return the list of unique cats along with their information
        return [
            dict(id=cat_id, name=cat_name, age=cat_age) for cat_id, cat_name, cat_age, *_ in cats_raw
            if cat_id not in cats_ids and not cats_ids.add(cat_id)
        ]
    except ValueError:
        # The file data does not meet the requirements or is corrupted
        # Raise exception to the upper level
        raise ValueError("The file data does not meet the requirements or is corrupted")
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))


def get_cats_info(cats_file: Union[Path, str]) -> list[dict[str, str]]:
    """Return the cats info based on data from the cats file

    :param cats_file: specified cats data file path (str, Path, mandatory)
    :return: cats info (list of dictionaries)
    """

    # Load the salaries data from the specified file
    cats: list[dict[str, str]] = get_cats(cats_file)

    # Return the cats info
    return cats
