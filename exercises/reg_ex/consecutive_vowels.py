import re

def consecutive_vowels(file_line):
    reg = re.compile("[A-Za-z]*[aeiouAEIOU]{1}[aeiouAEIOU]{1}[A-Za-z]*")
    return file_line if reg.findall(file_line) else None

try:
    file_handler = open("jumping_frog.txt")
except IOError:
    print("File not found or path is incorrect")
else:
    file = file_handler.read()
    print(consecutive_vowels(file))

    file_handler.close()