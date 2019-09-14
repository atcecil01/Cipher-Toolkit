print("================================================")
print("================================================")
print("=               Vigenere Cipher                =")
print("================================================")
print("================================================")

key = input("Enter key word or phrase(no numbers or symbols): ")
while shift.isalpha() == False:
    print("key must only be letters")
    key = input("Enter key word or phrase(no numbers or symbols): ")

message = input("Enter message to be enciphered(without punctuation): ")
newMessage = ""

print("Selected key: ", key)
print("Message: " + message)

for i in message:
    if i == " ":
        newVal = i
    elif i.isalpha():

# for i in message:
#     if i == " ":
#         newVal = i
#     elif i.isnumeric():
#         newVal = str((int(i) + int(shift)) % 10)
#     else:
#         value = (ord(i.lower()) - 97 + int(shift)) % 26
#         newVal = chr(value + 97)
#     newMessage += newVal

print("Cipher: " + newMessage)
choice = input('Enter "Q" to quit or any letter to return to the main menu: ')
if choice.lower() == "q":
    print("Exiting Cipher Toolkit...")