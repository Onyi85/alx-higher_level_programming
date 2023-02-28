#!/usr/bin/python3
"""This module provides a hands-on experience writing to a file"""


def write_file(filename="", text=""):
    """ This function writes to a file"""
    if filename:
        if text:
            with open(filename, 'w', encoding='utf-8') as fp:
                return (fp.write(text))
