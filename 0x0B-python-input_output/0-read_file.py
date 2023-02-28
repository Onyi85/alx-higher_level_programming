#!/usr/bin/python3
""" This module provides a hands-on experience on opening a file"""


def read_file(filename=""):
    """ This function reads the entire content of a file"""
    if filename:
        with open(filename, 'r', encoding='utf-8') as fp:
            text = fp.read()
            print(text, end='')
