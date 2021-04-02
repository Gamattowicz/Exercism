def is_isogram(string):
    string = string.lower().replace(" ", "").replace('-', '')
    s_string = set(string)
    return len(s_string) == len(string)


print(is_isogram('six-year-old'))
