import re

def is_allowed_specific_char(string):
    charRe = re.compile(r'[a-zA-Z0-9.]')
    string = charRe.search(string)
    return bool(string)

def has_vowel(string):
    pattern = re.compile(r'[aeiouAEIOU]')
    string = pattern.search(string)
    return  bool(string)

def is_integer(string):
    pattern = re.compile(r'^[-+]?[0-9]+$')
    string = pattern.search(string)
    return bool(string)


def is_fraction(string):
    pattern = re.compile(r'^[-+]?[0-9]+[/][0-9]+$')
    string = pattern.search(string)
    return bool(string)

def get_extention():
    with open(r'C:\Scripts\Python\regex-exercises-pycon2016\dictionary.txt') as dict_file:
        dictionary = dict_file.read()
        pattern = re.compile(r'')
