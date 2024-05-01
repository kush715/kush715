def caesar_cipher_encrypt(plaintext, shift):
    encrypted_message = ''
    for char in plaintext.upper():
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message
def caesar_cipher_decrypt(encrypted_message, shift):
    decrypted_message = ''
    for char in encrypted_message.upper():
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_message += shifted_char
        else:
            decrypted_message += char
    return decrypted_message
def main():
    plaintext = input("Enter the plaintext message: ")
    shift = int(input("Enter the shift value: "))
    encrypted_message = caesar_cipher_encrypt(plaintext, shift)
    print("Encrypted message:", encrypted_message)
    
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)
if __name__ == "__main__":
    main()
