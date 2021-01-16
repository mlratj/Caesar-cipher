import caesar_encryption


def decrypt(msg, key=None):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    options = len(letters)
    message = ""
    # works if a key is known
    if isinstance(key, int):
        for x in msg:
            y = x.upper()
            if y in letters:
                shift = letters.find(y)
                shift = shift - key
                if shift < 0:
                    shift = shift + options
                message = message + letters[shift]
            else:
                message = message + x
        print(message)
        return
    # checks every single letter in latin alphabet to decrypt a message
    for i in range(options):
        message = ""
        for x in msg:
            y = x.upper()
            if y in letters:
                shift = letters.find(y)
                shift = shift - i
                if shift < 0:
                    shift = shift + options
                message = message + letters[shift]
            else:
                message = message + x
        print(message)


# Example
'''
text = "Data is amazing"
shift = 4
key = 4
encrypted_msg = caesar_encryption.encrypt(text, 4)
decrypt(encrypted_msg)
'''
