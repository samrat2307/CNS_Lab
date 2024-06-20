import math

# Encryption
def encrypt(msg, key):
	cipher = ""

	# Track key indices
	k_idx = 0

	msg_len = float(len(msg))
	msg_lst = list(msg)
	key_lst = sorted(list(key))

	# Calculate column of the matrix
	col = len(key)
	
	# Calculate maximum row of the matrix
	row = int(math.ceil(msg_len / col))

	# Add the padding character '_' in empty cell of the matix
	fill_null = int((row * col) - msg_len)
	msg_lst.extend('_' * fill_null)

	# Create Matrix and insert message & padding characters row-wise
	matrix = [msg_lst[i: i + col]
			for i in range(0, len(msg_lst), col)]

	# Read matrix column-wise using key
	for _ in range(col):
		curr_idx = key.index(key_lst[k_idx])
		cipher += ''.join([row[curr_idx]
						for row in matrix])
		k_idx += 1

	return cipher

# Decryption
def decrypt(cipher, key):
	msg = ""

	# Track key indices
	k_idx = 0

	# Track msg indices
	msg_idx = 0
	msg_len = float(len(cipher))
	msg_lst = list(cipher)

	# Calculate column of the matrix
	col = len(key)
	
	# Calculate maximum row of the matrix
	row = int(math.ceil(msg_len / col))

	# Convert key into list and sort alphabetically (to access each character by its alphabetical position)
	key_lst = sorted(list(key))

	# Create an empty matrix to store deciphered message
	dec_cipher = []
	for _ in range(row):
		dec_cipher += [[None] * col]

	# Arrange the matrix column wise according to permutation order by adding into new matrix
	for _ in range(col):
		curr_idx = key.index(key_lst[k_idx])

		for j in range(row):
			dec_cipher[j][curr_idx] = msg_lst[msg_idx]
			msg_idx += 1
		k_idx += 1

	# Convert decrypted msg matrix into a string
	try:
		msg = ''.join(sum(dec_cipher, []))
	except TypeError:
		raise TypeError("This program cannot",
						"handle repeating words.")

	null_count = msg.count('_')

	if null_count > 0:
		return msg[: -null_count]

	return msg

# Main code
ch = int(input("What do you want to perform?\n1. Encryption\n2. Decryption\n"))

if(ch == 1):
    msg = str(input("Enter the message to be encrypted:\n"))
    key = str(input("Enter the key for encryption: "))
    print(f"Ciphertext is: {encrypt(msg, key)}")
elif(ch == 2):
    c_txt = str(input("Enter the ciphertext to be decrypted:\n"))
    key = str(input("Enter the key for decryption: "))
    print(f"Decrypted message is: {decrypt(c_txt, key)}")
else:
    print("Invalid input!")