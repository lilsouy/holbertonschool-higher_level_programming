#!/usr/bin/python3
"""
This module provides a function to print a text with two new lines
after each '.', '?', or ':' character.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.

    Doctests:
    >>> text_indentation("Hello. How are you?")
    Hello.
    
    How are you?
    >>> text_indentation("Python: is fun. Isn't it?")
    Python:
    
    is fun.
    
    Isn't it?
    >>> text_indentation(123)
    Traceback (most recent call last):
    TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_chars = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in end_chars:
            print(text[start:i+1].strip())
            print()
            start = i + 1
    if start < len(text):
        print(text[start:].strip())
