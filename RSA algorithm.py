# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP

# def generate_large_prime():
#     """
#     Generate large prime numbers p and q using RSA key generation.
#     """
#     key = RSA.generate(2048)
#     p = key.p
#     q = key.q
#     return p, q

# def calculate_totient(p, q):
#     """
#     Calculate Euler's totient function φ(n) for given prime numbers p and q.
#     """
#     return (p - 1) * (q - 1)

# def generate_keys(p, q):
#     """
#     Generate RSA public and private keys from prime numbers p and q.
#     """
#     n = p * q
#     totient = calculate_totient(p, q)
#     e = 65537  # commonly used value for e
#     d = pow(e, -1, totient)  # modular inverse of e modulo totient
#     public_key = RSA.construct((n, e))
#     private_key = RSA.construct((n, e, d))
#     return public_key, private_key

# def encrypt_message(message, public_key):
#     """
#     Encrypt a message using RSA encryption with OAEP padding.
#     """
#     cipher = PKCS1_OAEP.new(public_key)
#     ciphertext = cipher.encrypt(message)
#     return ciphertext

# def decrypt_message(ciphertext, private_key):
#     """
#     Decrypt a ciphertext using RSA decryption with OAEP padding.
#     """
#     cipher = PKCS1_OAEP.new(private_key)
#     plaintext = cipher.decrypt(ciphertext)
#     return plaintext

# def main():
#     # Generate large prime numbers p and q
#     p, q = generate_large_prime()
#     print("Generated primes p and q:", p, q)
    
#     # Generate public and private keys
#     public_key, private_key = generate_keys(p, q)
    
#     # Test encryption and decryption
#     message = b"Hello, RSA!"
#     print("Original message:", message)
    
#     # Encrypt the message using the public key
#     encrypted_message = encrypt_message(message, public_key)
#     print("Encrypted message:", encrypted_message.hex())
    
#     # Decrypt the message using the private key
#     decrypted_message = decrypt_message(encrypted_message, private_key)
#     print("Decrypted message:", decrypted_message.decode())

# if __name__ == "__main__":
#     main()
