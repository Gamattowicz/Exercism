def rotate(text, key):
    encode_text = ""
    for x in text:
        if x.isupper():
            encode_text += chr((ord(x) - 65 + key) % 26 + 65)
        elif x.islower():
            encode_text += chr((ord(x) - 97 + key) % 26 + 97)
        else:
            encode_text += x
    return encode_text




