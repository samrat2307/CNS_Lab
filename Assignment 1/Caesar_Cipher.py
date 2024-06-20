
# Ceaser cipher
import enchant

d = enchant.Dict("en_US")

def encrypt(text, shift):
    encrypted_txt = ""
 
    for i in range(len(text)):
        char = text[i]

        # Checking for valid input text
        if ord(char) in range(65,91) or ord(char) in range(97,123):
            # Encrypting Uppercase characters (A=65, B=66, ...)
            if (char.isupper()):
                encrypted_txt += chr((ord(char) + shift-65) % 26 + 65)
    
            # Encrypting Lowercase characters (a=97, b=98, ...)
            else:
                encrypted_txt += chr((ord(char) + shift-97) % 26 + 97)
        elif char == " ":
            encrypted_txt += " "
        else:
            encrypted_txt = f"Invalid character {char} in input string!\nOnly Alphabets [a-z][A-Z] are allowed"               
            break 
 
    return encrypted_txt

def decrypt(text, shift):
    decrypted_txt = ""
    shift = 26-shift
 
    for i in range(len(text)):
        char = text[i]

        # Checking for valid input text
        if ord(char) in range(65,91) or ord(char) in range(97,123):
            # Decrypting Uppercase characters
            if (char.isupper()):
                decrypted_txt += chr((ord(char) + shift-65) % 26 + 65)
            # Decrypting Lowercase characters
            else:
                decrypted_txt += chr((ord(char) + shift-97) % 26 + 97)
        elif char == " ":
                decrypted_txt += " "
        else:
            decrypted_txt = f"Invalid character {char} in input string!\nOnly Alphabets [a-z][A-Z] are allowed"               
            break 
 
    return decrypted_txt

def is_english_word(word):
    return d.check(word)

# Main Program
c = int(input("What do you want to perform?\n1. Encryption\n2. Decryption\n"))
if c==1:
    # Encryption
    txt = str(input("Enter the text to be encrypted: "))
    shift = int(input("Enter the shift: "))
    # Checking for valid shift value
    if shift in range(1, 26):
        print(f"Ciphertext is:\n{encrypt(txt, shift)}")
    else:
        print("Invalid Shift value !!\nValue must be in between 1-25")
elif c==2:
    # Decryption
    txt = str(input("Enter the text to be decrypted: "))
    shift_known = str(input("Do you know the shift value [y/n] ?  "))
    if shift_known == 'y':
        shift = int(input("Enter the shift: "))
        # Checking for valid shift value
        if shift in range(1, 26):
            print(f"Decrypted text is:\n{decrypt(txt, shift)}")
        else:
            print("Invalid Shift value !!\nValue must be in between 1-25")
    elif shift_known == 'n':
        dec_txt = []
        for shift in range(1, 26):
            dec_txt.append(decrypt(txt, shift))

        is_found = False
        for snt in dec_txt:
            correct_words = 0
            words = snt.split()

            for word in words:
                if is_english_word(word):
                    correct_words += 1

            if correct_words == len(words):
                is_found = True
                print(f"Most appropriate decrypted text is:\n{snt}\nShift used = {dec_txt.index(snt)+1}")

        if not is_found:
            print("Unable to find the appropriate match!\nList of all possible decrypted texts is:")
            for i, snt in enumerate(dec_txt):
                print(f"{i+1}. {snt}")

    else:
        print("Invalid input!")

else:
    print("Invalid input!")