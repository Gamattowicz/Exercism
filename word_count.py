from collections import Counter
import re


def count_words(sentence):
    return Counter([word.strip("'") for word in re.findall("[A-Za-z0-9']+",
                                                           sentence.lower())])