# -*- coding: utf-8 -*-"

"""
Core functions for task 04
"""

import sys
from typing import Optional
from colorama import Style, Fore
from pathlib import Path

from .futil import get_absolute_path, load_json_file_data, write_json_file_data


CONTACTS_FILE = get_absolute_path(Path(__file__).parent / "data" / "__contacts__.json")



def read_contacts_from_file() -> dict[str, str]:
    """Read contacts from a file

    :return data: contacts data (dictionary)
    """
    contacts: Optional[dict[str, str]] = load_json_file_data(CONTACTS_FILE, ignore_if_not_exist=True)
    return contacts if contacts is not None else {}


def write_contacts_to_file(contacts: dict[str, str]) -> None:
    """Write contacts to a file

    :param contacts: contacts data (dictionary, mandatory)
    """
    write_json_file_data(CONTACTS_FILE, contacts if contacts is not None else {})


def main() -> None:
    try:
        contacts: dict[str, str] = read_contacts_from_file()
    except Exception as e:
        print(Fore.RED + str(e))

    # Reset console styles to default
    print(Style.RESET_ALL)

    exit(0)


if __name__ == "__main__":
    main()
