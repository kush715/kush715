# from Crypto.Cipher import IDEA
# from Crypto.Random import get_random_bytes

# def generate_key():
#     return get_random_bytes(16)

# def generate_subkeys(main_key):
#     subkeys = []
#     for i in range(8):
#         subkey = main_key[i * 2: i * 2 + 2]
#         subkeys.append(int.from_bytes(subkey, byteorder='big'))
#     return subkeys

# def encrypt_block(block, subkeys):
#     cipher = IDEA.new(subkeys)
#     return cipher.encrypt(block)

# def decrypt_block(block, subkeys):
#     cipher = IDEA.new(subkeys)
#     return cipher.decrypt(block)

# def main():
#     # Generate a 128-bit key
#     key = generate_key()
#     print("Generated Key:", key.hex())
    
#     # Generate subkeys from the main key
#     subkeys = generate_subkeys(key)
#     print("Generated Subkeys:", subkeys)
    
#     # Test encryption and decryption
#     plaintext = b'Hello World!'
#     print("Plaintext:", plaintext)
    
#     # Pad the plaintext to ensure it's a multiple of 8 bytes
#     plaintext += b'\x00' * (8 - len(plaintext) % 8)
    
#     # Encrypt the plaintext
#     encrypted = encrypt_block(plaintext, subkeys)
#     print("Encrypted:", encrypted.hex())
    
#     # Decrypt the ciphertext
#     decrypted = decrypt_block(encrypted, subkeys)
#     print("Decrypted:", decrypted.rstrip(b'\x00'))

# if __name__ == "__main__":
#     main()
