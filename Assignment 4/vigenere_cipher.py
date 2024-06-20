# vigenere Generates key in a cyclic manner until it's length isn't equal to the length of original text
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
	
# Encryption
def encrypt(msg, key):
	cipher_text = []
	for i in range(len(msg)):
		x = (ord(msg[i]) +
			ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))
	
# Decryption
def decrypt(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))
	
# Main code
ch = int(input("What do you want to perform?\n1. Encryption\n2. Decryption\n"))

if(ch == 1):
    msg = str(input("Enter the message to be encrypted:\n"))
    keyword = str(input("Enter the keyword for encryption: "))
    key = generateKey(msg, keyword)
    print(f"Ciphertext is: {encrypt(msg, key)}")
elif(ch == 2):
    c_txt = str(input("Enter the ciphertext to be decrypted:\n"))
    keyword = str(input("Enter the keyword for decryption: "))
    key = generateKey(c_txt, keyword)
    print(f"Decrypted message is: {decrypt(c_txt, key)}")
else:
    print("Invalid input!")