import re

def find_dups(file_line):
    reg = re.compile(r"(\b\S+\b).*\b(\1)\b")
    return file_line if reg.search(file_line) else None

try:
    file_handler = open("jumping_frog.txt")
except IOError:
    print("File not found or path is incorrect")
else:
    for line in file_handler.readlines():
        found_line = find_dups(line)
        if found_line is not None:
            print(found_line)
