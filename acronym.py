import re


def abbreviate(words):
    result = ''
    for word in re.split(r"[-_\s]+", words):
        if word[0].isalpha():
            result += word[0].upper()
    return result