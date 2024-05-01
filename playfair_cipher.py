def generate_key_square(key):
    key = key.replace(" ", "").upper()
    key_square = ""
    for char in key:
        if char not in key_square:
            key_square += char
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in key_square:
            key_square += char
    return key_square
def get_coordinates(char, key_square):
    index = key_square.index(char)
    row = index // 5
    col = index % 5
    return row, col
def playfair_cipher_encrypt(plaintext, key):
    key_square = generate_key_square(key)
    plaintext = plaintext.replace(" ", "").upper()
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i+1]
        row1, col1 = get_coordinates(char1, key_square)
        row2, col2 = get_coordinates(char2, key_square)
        if row1 == row2:
            ciphertext += key_square[row1*5 + (col1 + 1) % 5]
            ciphertext += key_square[row2*5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_square[((row1 + 1) % 5)*5 + col1]
            ciphertext += key_square[((row2 + 1) % 5)*5 + col2]
        else:
            ciphertext += key_square[row1*5 + col2]
            ciphertext += key_square[row2*5 + col1]
    return ciphertext
key = "PLAYFAIR EXAMPLE"
plaintext = "HELLO WORLD"
encrypted_text = playfair_cipher_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)
