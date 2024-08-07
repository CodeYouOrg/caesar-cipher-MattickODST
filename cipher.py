# add your code here
user_input = input("Enter the sentence to be encrypted:")
encrypted_text = ""
for each_char in user_input:
    #checks if the character if an alpha character
    if 97 <= ord(each_char) <= 123:
        encrypted_char = ord(each_char) + 5
        #wraps around if the ord of a charcter goes past 123
        if encrypted_char > ord('z'):
            encrypted_char -= 26
        encrypted_text += chr(encrypted_char)
    else:
        encrypted_text += each_char
print('Encrypted text:')  
print(encrypted_text)