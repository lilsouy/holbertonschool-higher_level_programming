#!/usr/bin/python3
"""
This module provides a function to print a full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first_name> <last_name>.

    Args:
        first_name (str): First name
        last_name (str): Last name

    Raises:
        TypeError: If first_name or last_name is not a string.

    Doctests:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    >>> say_my_name(12, "White")
    Traceback (most recent call last):
    TypeError: first_name must be a string
    >>> say_my_name("John", 45)
    Traceback (most recent call last):
    TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}".strip())
