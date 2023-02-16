import re

def contains_alphabet(str):
    reg = re.compile('[a-z]+')
    return reg.findall(str) if reg.findall(str) else None

def match_g_and_r(str):
    reg = re.compile('g{1}r*')
    return reg.findall(str) if reg.findall(str) else None

def match_ac_b_and_q(str):
    reg = re.compile('ac{1}b+q+')
    return reg.findall(str) if reg.findall(str) else None

# Write a Python program to check that a string contains alphabetical characters using `re` and not the built in `isalpha()` method.
print(contains_alphabet("alphabet"))
print(contains_alphabet("01203"))

# Write a Python program that matches a string that has a `g` followed by zero or more `r`s.
print(match_g_and_r("grreaat"))
print(match_g_and_r("geaat"))
print(match_g_and_r("eaagrrt poprrgr"))
print(match_g_and_r("peter"))

# Write a Python program that matches a string that has an `ac` followed by one or more `b`s and then at least one `q` after the last `b`.
print(match_ac_b_and_q("acbq"))
print(match_ac_b_and_q("opopacbbqbbq"))
print(match_ac_b_and_q("opopacbbbb"))