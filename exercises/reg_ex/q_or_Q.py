import re

def q_or_Q(file_line):
    reg = re.compile(r"\b[qQ]{1}[a-zA-Z0-9]+\b")
    return file_line if reg.search(file_line) else None

try:
    file_handler = open("jumping_frog.txt")
except IOError:
    print("File not found or path is incorrect")
else:
    for line in file_handler.readlines():
        found_line = q_or_Q(line)
        if found_line is not None:
            print(found_line)
