'''
There is a technique for encrypting data that uses a single word as its key. 
First, choose a word as the key, such as TRAILBLAZERS. If the word contains repeated letters, keep only the first one, start the new alphabet with the result, 
and add the letters that do not appear in the new alphabet in the normal alphabetical order. As follows:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T R A I L B Z E S C D F G H J K M N O P Q U V W X Y
The rest is filled in with the remaining letters of the alphabet. When encrypting a message, 
each letter in the message is fixed to the top line and replaced by the corresponding letter in the bottom line (the case status of the letter character should be preserved). 
Therefore, with this key, the Attack AT DAWN is encrypted as Tpptad TP ITVH.
'''

def encrypt_message(key, plaintext):
    original_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = key + ''.join([c for c in original_alphabet if c not in key])
    char_map = dict(zip(original_alphabet, new_alphabet))

    encrypted_message = []
    for char in plaintext:
        if char.islower():
            encrypted_message.append(char_map[char])
        else:
            encrypted_message.append(char_map[char.lower()].upper())

    return ''.join(encrypted_message)

# Example
key = 'nihao'
plaintext = 'ni'
ciphertext = encrypt_message(key, plaintext)
print(ciphertext)
