input("\n\033[94mPress Any Key to Start...")
print("\033[90m=" * 80)

# Intro
import pyfiglet
greet = "GOOD DAY!"
print("\033[92m" + pyfiglet.figlet_format(greet, font = "bubble"))

#Pseudocode
#Define Variables
def remove_space(a):
    a = a.upper()
    for i in a:
        if " " in i:
            a = a.replace(i, "")
    print("\n\033[96mTranslated:", a)
    return a

def to_number(a, b):
    for i in a:
        if i in letter_to_number:
            b.append(letter_to_number[i])
 
def list_to_strings(a, b):
    for i in a:
        b = b + (str(i) + " ")
    return b
#Conversion
letter_to_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}
letter_to_number_rev = {number: letter for letter, number in letter_to_number.items()}

print("\033[90m=" * 80)
#User's inputted message
message = input("\n\033[92mYour Message: ")
message = remove_space(message)
#User's inputted key
key = input("\n\033[92mYour Key: ")
key = remove_space(key)

message_number, key_number, sum_number, mod_number = [], [], [], []
cipher, message_cipher, key_cipher, keys, messages, add, mod = "", "", "", "", "", "", ""

if len(key) < len(message):
    number_rep = len(message) // (len(key)) + 1
    messages = message
    keys = (key * number_rep)[:len(message)]
elif len(key) > len(message):
    number_rep = len(key) // (len(message)) + 1
    keys = key
    messages = (message * number_rep)[:len(key)]
else:
    keys = key
    messages = message

print("\033[90m=" *80)

to_number(messages, message_number)
to_number(keys, key_number)
#MESSAGE
print("\n\033[96mMESSAGE:", message, list_to_strings(message_number, message_cipher))
#KEY
#ADD
#MOD
#CIPHERTEX
