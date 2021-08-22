#!/usr/bin/python3
""" Import modules, sys and own functions """
from sys import argv
import json
save_to_json_file = __import__('3-save_to_json_file').save_to_json_file
load_from_json_file = __import__('4-load_from_json_file').load_from_json_file

try:
    j_list = load_from_json_file('add_item.json')
except:
    j_list = []

for i in range(1, len(argv)):
    j_list.append(argv[i])

save_to_json_file(j_list, 'add_item.json')
