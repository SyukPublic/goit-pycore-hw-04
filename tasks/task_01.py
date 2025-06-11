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

    # Load the salaries data from the file and prepare
    salaries_raw: list[tuple[str, ...]] = [
        tuple(data_row.strip().split(",")) for data_row in load_text_file_data(get_absolute_path(salaries_file))
    ]
    salaries: list[tuple[str, float]] = [(name, float(salary)) for name, salary, *_ in salaries_raw]

    # Return salaries
    return salaries



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
