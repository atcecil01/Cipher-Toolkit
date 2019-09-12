
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
            # Check if shift is an integer: IF STATEMENT IS NOT WORKING ????????????????????????????????????????
            if shift.isnumeric == False:
                print("shift must be a whole number")
                shift = input("Enter cipher shift (1-25): ")

            message = input("Enter message to be enciphered: ")
            newMessage = ""

            print("Selected shift: ", shift)
            print("Message: " + message)


            # For all letters: 
            # Check if valid #
            # newLetter = (ord(letter) - 96 + shift)

            for i in message:
                newVal  = (ord(i) - 96 + shift)
                print(newVal)

            print(newMessage)
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


    # print("================================================")
    # print("================================================")
    # print("=                CaesarCipher                  =")
    # print("================================================")
    # print("================================================")

    # shift = input("Enter cipher shift (1-25): ")
    # # Check if shift is an integer: IF STATEMENT IS NOT WORKING ????????????????????????????????????????
    # if shift.isnumeric == False:
    #     print("shift must be a whole number")
    #     shift = input("Enter cipher shift (1-25): ")

    # message = input("Enter message to be enciphered: ")
    # newMessage = ""

    # print("Selected shift: ", shift)
    # print("Message: " + message)


    # # For all letters: 
    # # Check if valid #
    # # newLetter = (ord(letter) - 96 + shift)

    # for i in message:
    #     newVal  = (ord(i) - 96 + shift)
    #     print(newVal)

    # print(newMessage)