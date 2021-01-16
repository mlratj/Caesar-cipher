def encrypt(plain_text, shift):
    """ Uses a shift argument to swap every letter of a given text """
    secret = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isupper():
            secret += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            secret += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            secret += char
    return secret


# Example
'''
text = "Data is amazing"
encryption_shift = 4
print(encrypt(text, encryption_shift))
'''
