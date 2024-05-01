def monoalphabetic_cipher_encrypt(plaintext, mapping):
    plaintext = plaintext.upper()
    encrypted_message = ''
    for char in plaintext:
        if char.isalpha():
            encrypted_message += mapping[char]
        else:
            encrypted_message += char
    return encrypted_message
def monoalphabetic_cipher_decrypt(encrypted_message, inverse_mapping):
    decrypted_message = ''
    for char in encrypted_message.upper():
        if char.isalpha():
            decrypted_message += inverse_mapping[char]
        else:
            decrypted_message += char
    return decrypted_message
def main():
    mapping = {
        'A': 'Q', 'B': 'Z', 'C': 'R', 'D': 'T', 'E': 'Y', 'F': 'U', 'G': 'P',
        'H': 'S', 'I': 'O', 'J': 'K', 'K': 'W', 'L': 'X', 'M': 'V', 'N': 'N',
        'O': 'M', 'P': 'B', 'Q': 'C', 'R': 'D', 'S': 'E', 'T': 'F', 'U': 'G',
        'V': 'H', 'W': 'I', 'X': 'J', 'Y': 'A', 'Z': 'L'
    }
    inverse_mapping = {v: k for k, v in mapping.items()}
    plaintext = input("Enter the plaintext message: ")
    encrypted_message = monoalphabetic_cipher_encrypt(plaintext, mapping)
    print("Encrypted message:", encrypted_message)
    decrypted_message = monoalphabetic_cipher_decrypt(encrypted_message, inverse_mapping)
    print("Decrypted message:", decrypted_message)
if __name__ == "__main__":
    main()
