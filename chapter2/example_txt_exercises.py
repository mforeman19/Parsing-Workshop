import re
import io

def count_alpha_words(file):
    reg = re.compile('\\b[^0-9][a-zA-Z]+\\b')
    return len(reg.findall(file)) if reg.findall(file) else None

def sum_file_ints(file):
    reg = re.compile('[0-9]+')
    match_list = reg.findall(file)
    total = 0
    for i in match_list:
        total += int(i)
    return total

def find_string_in_file(file_line, str):
    reg = re.compile(f"{str)}")
    return file_line if reg.search(file_line) else None

try:
    file_handler = open("example.txt")
except IOError:
    print("File not found or path is incorrect")
else:
    file = file_handler.read()
    print(count_alpha_words(file))
    print(sum_file_ints(file))

    file_handler.close()

try:
    file_handler = open("example.txt")
except IOError:
    print("File not found or path is incorrect")
else:
    for line in file_handler.readlines():
        if find_string_in_file(line, "and") is not None:
            print(find_string_in_file(line, "and"))

    file_handler.close()