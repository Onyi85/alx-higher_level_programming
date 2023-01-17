#!/usr/bin/python3
""" This module prints a text with 2 new lines after each
of these characters '. ? and :
"""


def text_indentation(text):
    """ This function prints a text with 2 new lines after
    each of these characters '.?:'
    """
    # --- checking if not string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # replace each punctuatin with the same plus two new lines

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    # printing the text with 2 new lines after each characters
    print("\n".join([line.strip() for line in text.split("\n")]), end="")
