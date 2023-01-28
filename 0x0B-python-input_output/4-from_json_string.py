#!/usr/bin/python3
""" This module converts from json format to python string """


import json
""" importing the json module """


def from_json_string(my_str):
    """ This function converts a json string to the python
    data structure specified
    """
    return (json.loads(my_str))
