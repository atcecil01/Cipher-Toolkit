
choice = ""
while choice.lower() != "q":
    print("================================================")
    print("================================================")
    print("=                Cipher Toolkit                =")
    print("================================================")
    print("================================================")
    print("\n")
    print("Main Menu:")
    print("================================================")
    print("1. Encipher Message")
    print("2. Decipher Message")
    print("3. Crack a Cipher -- UNDER DEVELOPMENT")
    print("\n")

    choice = input('Enter a number to select an Option, or enter "Q" to quit: ')

    if choice == "1":
        print("\n")
        print("Cipher Menu")
        print("============================================")
        print("1. Caesar Cipher")
        print("2. Playfair Cipher -- UNDER DEVELOPMENT")
        print("3. Vigenere Cipher -- UNDER DEVELOPMENT")
        print("4. Transposition Cipher -- UNDER DEVELOPMENT")
        print("5. One Time Pad -- UNDER DEVELOPMENT")
        print("\n")
        cipherChoice = input("Enter a number to select a cipher: ")
        if cipherChoice == "1":
            print("================================================")
            print("================================================")
            print("=                CaesarCipher                  =")
            print("================================================")
            print("================================================")

            shift = input("Enter cipher shift (1-25): ")
            while shift.isnumeric() == False:
                print("shift must be a whole number")
                shift = input("Enter cipher shift (1-25): ")

            message = input("Enter message to be enciphered(without punctuation): ")
            newMessage = ""

            print("Selected shift: ", shift)
            print("Message: " + message)

            for i in message:
                if i == " ":
                    newVal = i
                elif i.isnumeric():
                    newVal = str((int(i) + int(shift)) % 10)
                else:
                    value = (ord(i) - 97 + int(shift)) % 26
                    newVal = chr(value + 97)
                newMessage += newVal

            print("Cipher: " + newMessage)
            choice = input('Enter "Q" to quit or any letter to return to the main menu: ')
            if choice.lower() == "q":
                print("Exiting Cipher Toolkit...")
    elif choice == "2":
        print("\n")
        print("DeCipher Menu")
        print("============================================")
        print("1. Caesar Cipher")
        print("2. Playfair Cipher -- UNDER DEVELOPMENT")
        print("3. Vigenere Cipher -- UNDER DEVELOPMENT")
        print("4. Transposition Cipher -- UNDER DEVELOPMENT")
        print("5. One Time Pad -- UNDER DEVELOPMENT")
        print("\n")
        decipherChoice = input("Enter a number to select a cipher: ")
        # if decipherChoice == "1"
    elif choice == "3":
        print("This option is still under development")
    elif choice.lower() == "q":
        print("Exiting Cipher Toolkit...")
    else:
        print("Please enter a valid option by typing the number of the menu option you would like to choose")
