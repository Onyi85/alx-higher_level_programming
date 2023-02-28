#!/usr/bin/python3
""" This module reads from a json file """


import json
"""Importing the json module """


def load_from_json_file(filename):
    """ This function creats an objects from a json file to a
    file"""
    with open(filename) as fp:
        text = fp.read()
        return json.loads(text)
