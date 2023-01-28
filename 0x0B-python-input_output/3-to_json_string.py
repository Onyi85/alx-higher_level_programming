#!/usr/bin/python3
""" This module converts python string to json format """


import json
""" importing the json module"""


def to_json_string(my_obj):
    """ This function returns a python string as a json format"""
    return (json.dumps(my_obj))
