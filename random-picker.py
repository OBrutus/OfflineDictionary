#!/bin/python3
from difflib import get_close_matches
import json
from random import randint

# path_to_json = '$HOME/.Dictionary_AV/'
path_to_json = "data.json"
data = json.load(open(path_to_json))

space = list(data.keys())
index = randint(0, len(space))
word = space[index]

print('''
Word     : '''+ word +'''
Meaning  : '''+ data.get(word)[0] +'''
''')