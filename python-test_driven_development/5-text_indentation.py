#!/usr/bin/python3

def text_indentation(text):
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
