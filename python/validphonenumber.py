"""
ID: happyn61
LANG: PYTHON3
PROB: namenum
"""
import re
with open('file.txt') as f:
    content = f.readlines()
    for c in content:
        if len(c.strip())==12 and re.match("[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]",c):
            print(c.strip())
        if len(c.strip())==14 and re.match("\([0-9][0-9][0-9]\) [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]",c):
            print(c.strip())
