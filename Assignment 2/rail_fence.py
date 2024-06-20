# railfencnce print
def encryptRailFence(text, key):

	
	rail = [['*' for i in range(len(text))]
				for j in range(key)]
	
	dir_down = False
	row, col = 0, 0
	
	for i in range(len(text)):
		
		
		if (row == 0) or (row == key - 1):
			dir_down = not dir_down
		
		rail[row][col] = text[i]
		col += 1
		
		if dir_down:
			row += 1
		else:
			row -= 1
	
	result = []
	for i in range(key):
		for j in range(len(text)):
			print(rail[i][j],end=" ")
			if rail[i][j] != '*':
				result.append(rail[i][j])
		print()
	return("" . join(result))

	

def decryptRailFence(cipher, key):

	rail = [['\n' for i in range(len(cipher))]
				for j in range(key)]
	
	
	dir_down = None
	row, col = 0, 0
	
	
	for i in range(len(cipher)):
		if row == 0:
			dir_down = True
		if row == key - 1:
			dir_down = False
		
		rail[row][col] = '*'
		col += 1
		
		if dir_down:
			row += 1
		else:
			row -= 1
	
	index = 0
	for i in range(key):
		for j in range(len(cipher)):
			if ((rail[i][j] == '*') and
			(index < len(cipher))):
				rail[i][j] = cipher[index]
				index += 1
	
	result = []
	row, col = 0, 0
	for i in range(len(cipher)):
		
		if row == 0:
			dir_down = True
		if row == key-1:
			dir_down = False
		
		if (rail[row][col] != '*'):
			result.append(rail[row][col])
			col += 1
			
		
		if dir_down:
			row += 1
		else:
			row -= 1
	return("".join(result))

# Driver code
if __name__ == "__main__":
	c = int(input("What do you want to perform?\n1. Encryption\n2. Decryption\n"))
	if c==1:
		txt = str(input("Enter the text to be encrypted: "))
		shift = int(input("Enter the Key: "))
		print(f"Ciphertext is:\n{encryptRailFence(txt, shift)}")

	elif c==2:
		# Decryption
		txt = str(input("Enter the text to be decrypted: "))
		shift = int(input("Enter the Key: "))
		print(f"Ciphertext is:\n{decryptRailFence(txt, shift)}")