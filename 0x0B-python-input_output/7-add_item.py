#!/usr/bin/python3
"""This module adds all the arguments to a python list and then
   saves them to a file"""
import sys
import json
""" importing the modules """

# Importing the save and load modules
save_to_json_file = __import__("5-save_to_json_file")\
        .save_to_json_file
load_from_json_file = __import__("6-load_from_json_file")\
        .load_from_json_file
filename = "add_item.json"

try:
    arguments = load_from_json_file("add_item.json")
except Exception:   # file doesn't exist create an empty list
    arguments = []
# find the length of arguments
args_len = len(sys.argv)
for i in range(1, args_len):
    arguments.append(sys.argv[i])
save_to_json_file(arguments[:], filename)
