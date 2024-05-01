import random
def generate_key():
    key = list(range(26))
    random.shuffle(key)
    return key
def encrypt(plaintext, key):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += chr((key[ord(char) - ord('a')]) + ord('a'))
            else:
                ciphertext += chr((key[ord(char) - ord('A')]) + ord('A'))
        else:
            ciphertext += char
    return ciphertext
def generate_plain_text_pair():
    plain_text1 = ''.join([chr(random.randint(97, 122)) for _ in range(8)]) # 8 characters plaintext
    plain_text2 = ''.join([chr(random.randint(97, 122)) for _ in range(8)])
    return plain_text1, plain_text2
def differential_cryptoanalysis(ciphertext, num_iterations=1000):
    differences = {}
    for _ in range(num_iterations):
        plain_text1, plain_text2 = generate_plain_text_pair()
        cipher1 = encrypt(plain_text1, key)
        cipher2 = encrypt(plain_text2, key)
        diff = ''.join([bin(ord(cipher1[i]) ^ ord(cipher2[i]))[2:].zfill(8) for i in range(len(cipher1))])
        if diff in differences:
            differences[diff] += 1
        else:
            differences[diff] = 1
    max_diff = max(differences, key=differences.get)
    return max_diff, differences[max_diff]
key = generate_key()
plaintext = "hello"
ciphertext = encrypt(plaintext, key)
max_diff, count = differential_cryptoanalysis(ciphertext)
print("Most frequent differential:", max_diff)
print("Occurrence count:", count)
