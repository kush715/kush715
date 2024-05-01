# from Crypto.Cipher import Blowfish
# from Crypto.Random import get_random_bytes

# def encrypt_message(key, plaintext):
#     cipher = Blowfish.new(key, Blowfish.MODE_ECB)
#     ciphertext = cipher.encrypt(plaintext)
#     return ciphertext

# def decrypt_message(key, ciphertext):
#     cipher = Blowfish.new(key, Blowfish.MODE_ECB)
#     plaintext = cipher.decrypt(ciphertext)
#     return plaintext

# def main():
#     key = get_random_bytes(16)  # Generate a random 16-byte key
#     plaintext = b"Hello, Blowfish!"  # Convert message to bytes
    
#     # Encrypt the message
#     ciphertext = encrypt_message(key, plaintext)
#     print("Encrypted message:", ciphertext.hex())
    
#     # Decrypt the message
#     decrypted_message = decrypt_message(key, ciphertext)
#     print("Decrypted message:", decrypted_message.decode())

# if __name__ == "__main__":
#     main()
