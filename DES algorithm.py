# from Crypto.Cipher import DES
#  from Crypto.Random import get_random_bytes

# def encrypt_message(message, key):
#     cipher = DES.new(key, DES.MODE_ECB)
#     ciphertext = cipher.encrypt(message)
#     return ciphertext

# def decrypt_message(ciphertext, key):
#     cipher = DES.new(key, DES.MODE_ECB)
#     decrypted_message = cipher.decrypt(ciphertext)
#     return decrypted_message

# def main():
#     key = get_random_bytes(8)  # Generate a random 8-byte key
#     message = b"Hello, DES!"  # Convert message to bytes

#     # Encrypt the message
#     ciphertext = encrypt_message(message, key)
#     print("Encrypted message:", ciphertext.hex())

#     # Decrypt the message
#     decrypted_message = decrypt_message(ciphertext, key)
#     print("Decrypted message:", decrypted_message.decode())

# if __name__ == "__main__":
#     main()
