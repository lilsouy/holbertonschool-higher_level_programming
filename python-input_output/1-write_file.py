#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)"""
    with open(filename, "w", encoding="utf-8")as file:
        return file.write(text)
