#!/usr/bin/python3

"""
This is "4-text_indentation" module

The module supplies the text_indentation function, which prints a text with 2 new lines after each of these characters: ., ? and :.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n\n", end="")
