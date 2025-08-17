import random
import string

sentence = " " + string.punctuation + string.digits +string.ascii_letters

sentence = list(sentence)
key = sentence.copy()

random.shuffle(key)

#print(sentence)
#print(key)

#Encryption********************************************************************************

Message = input("Enter your message to enrpyt: ")
cipher_text = ""


for letter in Message:
    index = sentence.index(letter)
    cipher_text += key[index]

print(f"Your Original message is :{Message}")
print(f"Your Encrypted Message is :{cipher_text}")

#Decryption**********************************************************************************

cipher_text = input("Enter your message to enrpyt: ")
Message = ""


for letter in cipher_text:
    index = key.index(letter)
    Message += sentence[index]


print(f"Your Encrypted Message is :{cipher_text}")
print(f"Your Decrypted message is :{Message}")


## this is new line
