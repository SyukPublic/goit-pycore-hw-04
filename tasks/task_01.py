# -*- coding: utf-8 -*-"

"""
Core functions for task 01
"""

from typing import Union
from pathlib import Path

from .futil import get_absolute_path, load_text_file_data


def get_salaries(salaries_file: Union[Path, str]) -> list[tuple[str, float]]:
    """Load salaries from the given file

    :param salaries_file: specified salaries data file path (str, Path, mandatory)
    :return: salaries data (list of tuples)
    """

    # Load the salary data from the file, remove any empty lines, and prepare the information for further analysis
    try:
        salaries_raw: list[tuple[str, ...]] = [
            tuple(data_row.strip().split(","))
            for data_row in load_text_file_data(get_absolute_path(salaries_file), remove_empty_lines=True)
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
        # Prepare and return salaries
        return [(name, float(salary)) for name, salary, *_ in salaries_raw]
    except ValueError:
        # The file data does not meet the requirements or is corrupted
        # Raise exception to the upper level
        raise ValueError("The file data does not meet the requirements or is corrupted")
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))


def total_salary(salaries_file: Union[Path, str]) -> tuple[float, float]:
    """Calculate the total and average salary based on data from the salaries file

    :param salaries_file: specified salaries data file path (str, Path, mandatory)
    :return: total and average salary (tuple of floats)
    """

    # Load the salaries data from the specified file
    salaries: list[tuple[str, float]] = get_salaries(salaries_file)

    # Calculate the total and average salary
    total: float = sum([salary for _, salary in salaries])
    average: float = total / len(salaries) if len(salaries) > 0 else 0

    # Return the total and average salary
    return total, average
