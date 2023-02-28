#!/usr/bin/python3
"""This module writes to a file without overwriting the content"""


def append_write(filename="", text=""):
    """This function writes to a file without deleting its content"""
    if filename:
        if text:
            with open(filename, 'a', encoding="utf-8") as fp:
                return(fp.write(text))
