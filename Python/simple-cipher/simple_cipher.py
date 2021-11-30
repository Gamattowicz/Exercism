from random import choices
from string import ascii_lowercase


class Cipher:
    def __init__(self, key=None):
        if not key:
            key = "".join(choices(ascii_lowercase, k=100))
        self.key = key

    def encode(self, text):
        encoded = ""
        if len(self.key) < len(text):
            self.key *= len(text) // len(self.key) + 1
        for key, letter in zip(self.key, text):
            encoded += chr((ord(letter) - 97 + ord(key) - 97) % 26 + 97)

        return encoded

    def decode(self, text):
        decoded = ""
        if len(self.key) < len(text):
            self.key *= len(text) // len(self.key) + 1
        for key, letter in zip(self.key, text):
            decoded += chr((ord(letter) - 97 - ord(key) + 97) % 26 + 97)

        return decoded

cipher = Cipher("abc")
plaintext = "iamapandabear"
print(cipher.encode(plaintext))