def rotate_left(val, r_bits, max_bits=32):
    return ((val << r_bits) & (2 ** max_bits - 1)) | (val >> (max_bits - r_bits))
def rotate_right(val, r_bits, max_bits=32):
    return (val >> r_bits) | ((val << (max_bits - r_bits)) & (2 ** max_bits - 1))
def expand_key(key, word_size=32, rounds=12):
    key_size = len(key)
    mod_val = (rounds + 1) * 2
    if key_size % word_size != 0:
        key += b'\x00' * (word_size - key_size % word_size)
    L = [int.from_bytes(key[i:i+4], byteorder='little') for i in range(0, len(key), 4)]
    c = max(len(L), 1)
    S = [(i * 2 * word_size) % (2 ** word_size) for i in range(mod_val)]
    L_len = len(L)
    A, B = 0, 0
    for i in range(3 * max(L_len, c)):
        A = S[i % mod_val] = rotate_left((S[i % mod_val] + A + B) & (2 ** word_size - 1), 3)
        B = L[i % L_len] = rotate_left((L[i % L_len] + A + B) & (2 ** word_size - 1), (A + B) & (word_size - 1))
    return S
def encrypt_block(plaintext, key, word_size=32, rounds=12):
    A, B = plaintext
    S = expand_key(key, word_size, rounds)
    A = (A + S[0]) & (2 ** word_size - 1)
    B = (B + S[1]) & (2 ** word_size - 1)
    for i in range(1, rounds + 1):
        A = (rotate_left((A ^ B), B, word_size) + S[i * 2]) & (2 ** word_size - 1)
        B = (rotate_left((B ^ A), A, word_size) + S[i * 2 + 1]) & (2 ** word_size - 1)
    return A, B
def decrypt_block(ciphertext, key, word_size=32, rounds=12):
    A, B = ciphertext
    S = expand_key(key, word_size, rounds)
    for i in range(rounds, 0, -1):
        B = rotate_right((B - S[i * 2 + 1]) & (2 ** word_size - 1), A, word_size) ^ A
        A = rotate_right((A - S[i * 2]) & (2 ** word_size - 1), B, word_size) ^ B
    B = (B - S[1]) & (2 ** word_size - 1)
    A = (A - S[0]) & (2 ** word_size - 1)
    return A, B
def rc5_encrypt(plaintext, key, word_size=32, rounds=12):
    block_size = 8  # Size of each block in bytes (32-bit words)
    num_blocks = len(plaintext) // block_size + (1 if len(plaintext) % block_size != 0 else 0)
    ciphertext = b''
    for block_index in range(num_blocks):
        start_index = block_index * block_size
        end_index = min((block_index + 1) * block_size, len(plaintext))
        block = plaintext[start_index:end_index]
        if len(block) < block_size:
            block += bytes([0] * (block_size - len(block)))
        block_int = int.from_bytes(block, byteorder='little')
        encrypted_block = encrypt_block((block_int, 0), key, word_size, rounds)  # Adjusted function call
        ciphertext += b''.join(encrypted_block.to_bytes(8, byteorder='little'))
    return ciphertext
def rc5_decrypt(ciphertext, key, word_size=32, rounds=12):
    ciphertext = [int.from_bytes(ciphertext[i:i+4], byteorder='little') for i in range(0, len(ciphertext), 4)]
    plaintext = b''
    for block in ciphertext:
        decrypted_block = decrypt_block(block, key, word_size, rounds)
        plaintext += b''.join(decrypted_block.to_bytes(4, byteorder='little'))
    return plaintext
def main():
    key = b'SecretKey'
    plaintext = b'Hello, RC5!'
    ciphertext = rc5_encrypt(plaintext, key)
    print("Encrypted:", ciphertext.hex())
    decrypted_text = rc5_decrypt(ciphertext, key)
    print("Decrypted:", decrypted_text.decode())
if __name__ == "__main__":
    main()
