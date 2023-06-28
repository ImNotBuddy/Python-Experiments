import random
import string
import sys

import pyperclip

def main():
    characterList = ""
    password = []

    try:
        autoCopy = str(input("Would you like to auto copy to clipboard? (y/n): ")).lower()
        passwordLength = int(input("Please enter a length for the password: "))

        print('''Choose character set's for the password
    1. Letters
    2. Digits
    3. Special Characters
    4. All of the above
    5. Exit selection and generate password''')
        
        for x in range(3):
            characterSet = int(input("Please choose a character set: "))
            
            if characterSet == 1:
                characterList += string.ascii_letters
            elif characterSet == 2:
                characterList += string.digits
            elif characterSet == 3:
                characterList += string.punctuation
            elif characterSet == 4:
                characterList += string.ascii_letters
                characterList += string.digits
                characterList += string.punctuation
                break
            else:
                break
        
        for x in range(passwordLength):
            randomCharacter = random.choice(characterList)
            password.append(randomCharacter)

        password = "".join(password)

        print(f"Your generated password is: {password}")

        if autoCopy == "y":
            pyperclip.copy(password)

    except Exception as e:
        print(f"Something went wrong: {e}")
        sys.exit()

if __name__ == "__main__":
    main()