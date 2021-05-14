def rotate(text, key):
    result = ''
    if key == 0 or key == 26:
        return text
    else:
        for letter in text:
            if letter.isupper():
                result += chr((ord(letter) + key - 65) % 26 + 65)
            elif letter.islower():
                result += chr((ord(letter) + key - 97) % 26 + 97)
            else:
                result += letter
        return result




