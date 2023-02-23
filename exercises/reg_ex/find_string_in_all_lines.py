import re

def find_string_in_file(file_line, str):
    reg = re.compile(f"{str}")
    return file_line if reg.search(file_line) else None

try:
    file_handler = open("jumping_frog.txt")
except IOError:
    print("File not found or path is incorrect")
else:
    for line in file_handler.readlines():
        found_line = find_string_in_file(line, "q")
        if found_line is not None:
            print(found_line)
