import re


def abbreviate(words):
    return ''.join([word[0].upper() for word in re.split(r"[-_\s]+", words)
                    if word[0].isalpha()])