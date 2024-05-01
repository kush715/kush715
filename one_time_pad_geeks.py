def stringEncryption(text, key):
	cipherText = ""
	cipher = []
	for i in range(len(key)):
		cipher.append(ord(text[i]) - ord('A') + ord(key[i])-ord('A'))
		for i in range(len(key)):
			if cipher[i] > 25:
				cipher[i] = cipher[i] - 26



	for i in range(len(key)):
		x = cipher[i] + ord('A')
		cipherText += chr(x)

	
	return cipherText
def stringDecryption(s, key):

	
	plainText = ""

	

	plain = []

	# Running for loop for each character
	# subtracting and storing in the array

	for i in range(len(key)):
		plain.append(ord(s[i]) - ord('A') - (ord(key[i]) - ord('A')))

	# If the difference is less than 0
	# add 26 and store it in the array.
	for i in range(len(key)):
		if (plain[i] < 0):
			plain[i] = plain[i] + 26

	# Converting int to corresponding char
	# add them up to plainText

	for i in range(len(key)):
		x = plain[i] + ord('A')
		plainText += chr(x)

	# Returning plainText
	return plainText

plainText = "HowAreyou"
key = "NCBTZQARX"
encryptedText = stringEncryption(plainText.upper(), key.upper())
print("Cipher Text - " + encryptedText)
print("Message - " + stringDecryption(encryptedText, key.upper()))

# This code is contributed by Pranay Arora
