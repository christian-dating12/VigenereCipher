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
#User's inputted message
#User's inputted key
#MESSAGE
#KEY
#ADD
#MOD
#CIPHERTEX
