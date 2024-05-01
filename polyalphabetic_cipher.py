def polyalphabetic_cipher_encrypt(plaintext, key):
    key = key.upper()
    plaintext = plaintext.upper().replace(" ", "")
    key_length = len(key)
    encrypted_text = ""
    for i in range(len(plaintext)):
        shift = ord(key[i % key_length]) - ord('A')
        encrypted_char = chr(((ord(plaintext[i]) - ord('A') + shift) % 26) + ord('A'))
        encrypted_text += encrypted_char
    return encrypted_text
def main():
    plaintext = input("Enter the plaintext message: ")
    key = input("Enter the key: ")
    encrypted_text = polyalphabetic_cipher_encrypt(plaintext, key)
    print("Encrypted message:", encrypted_text)
if __name__ == "__main__":
    main()
