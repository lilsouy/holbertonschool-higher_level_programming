#!/usr/bin/python3
"""
Module for text indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ?, :
    No space at the beginning or end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    separators = ".?:"
    while i < length:
        line = ""
        while i < length and text[i] not in separators:
            line += text[i]
            i += 1
        if line:
            print(line.strip())
        if i < length and text[i] in separators:
            print(text[i])
            i += 1
        print()  # add 2 new lines total, current print adds 1
        while i < length and text[i] == " ":
            i += 1
