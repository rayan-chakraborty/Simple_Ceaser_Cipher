
#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 
#check the above function
print("Enter File Name to Be Encrypted")
file_name = input()
file = open(file_name + '.txt','r')
text = file.read()

s = 4
print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text,s))
