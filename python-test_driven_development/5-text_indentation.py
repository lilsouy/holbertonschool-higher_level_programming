#!/usr/bin/python3
"""Module that provides a function to print text with 2 new lines
after each '.', '?', or ':' character.
"""

def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', or ':' character.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in separators:
            line = text[start:i + 1].strip()
            print(line)
            print()
            start = i + 1

    if start < len(text):
        line = text[start:].strip()
        if line:
            print(line)
