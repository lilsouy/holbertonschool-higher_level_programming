#!/usr/bin/python3
"""Defines a function that appends text to a file."""


def append_write(filename="", text=""):
    """Append a string to a UTF8 text file and return chars count."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
