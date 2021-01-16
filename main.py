import caesar_encryption
import caesar_decryption


def main(plain_text, shift, key=None):
    encrypted_msg = caesar_encryption.encrypt(text, shift)
    decrypted_msg = caesar_decryption.decrypt(encrypted_msg, key)
    return encrypted_msg, decrypted_msg


if __name__ == '__main__':
    text = "Data is amazing"
    encryption_shift = 20
    test_key = 20
    # delete test_key argument to see all possible outputs of implemented decryption
    main(text, encryption_shift, test_key)