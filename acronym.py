import re


def abbreviate(words):
    return ''.join([word[0] for word in re.findall(r"[A-Z']+", words.upper())])