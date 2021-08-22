#!/usr/bin/python3
"""Defines the function"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and returns
    the number of characters added.

    Args:
        filename (str): Name of the file to be opened/created
        text (str): Text that will be inserted into the file
    Returns:
        Number of characters added into the file
    """
    with open(filename, 'a') as f:
        return(f.write(text))
