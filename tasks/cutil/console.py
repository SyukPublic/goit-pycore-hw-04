# -*- coding: utf-8 -*-"

"""
Functions for works with the console input/output
"""

from typing import Union
from colorama import Style, Fore


def console_style_reset() -> None:
    """Reset console output to defaults
    """
    print(Style.RESET_ALL)


def print_colored(fore: Fore, *args) -> None:
    """Print colored text to the console output

    :param fore: specified path (str, Path, mandatory)
    :param args: arguments to print (tuple of strings)
    """
    print(fore + " ".join([*args]), Style.RESET_ALL)


def print_error(error: Union[str, Exception]) -> None:
    """Print RED colored text to the console output

    :param error: error to print (string, Exception)
    """
    print_colored(Fore.RED, str(error) if isinstance(error, Exception) else error)


def print_welcome(text: str) -> None:
    """Print GREEN colored welcome text to the console output

    :param text: text  to print (string)
    """
    print()
    print_colored(Fore.GREEN, text)
    print()


def print_exit(text: str) -> None:
    """Print YELLOW colored exit text to the console output

    :param text: text  to print (string)
    """
    print()
    print_colored(Fore.YELLOW, text)
    print()


def print_help(text: str) -> None:
    """Print BLUE colored help text to the console output

    :param text: text  to print (string)
    """
    print()
    print_colored(Fore.BLUE, "#" * 60)
    print_colored(Fore.BLUE, text)
    print_colored(Fore.BLUE, "#" * 60)
    print()
