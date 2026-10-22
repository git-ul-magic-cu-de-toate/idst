
import sys

dictionary = {
    # 'A' : unused
     'B' : 'D',
    # 'C' : unused
     'D' : 'X',
     'E' : 'V',
     'F' : 'H',
     'G' : 'B',
     'H' : 'G',
     'I' : 'A',
     'J' : 'S',
     'K' : 'F',
     'L' : 'O',
     'M' : 'J',
     'N' : 'K',
     'O' : 'T',
    # 'P' : unused
     'Q' : 'P',
     'R' : 'W',
     'S' : 'N',
     'P' : 'I',
     'U' : 'E',
     'T' : 'R',
     'V' : 'L',
     'W' : 'C',
     'X' : 'U',
     'Y' : 'Y',
     'Z' : 'M'
            }

function = open("uncrackable.txt", "r")

text = function.read()

v = []

for letter in text:
    if letter in dictionary:
        v.append("\033[1;31m" + dictionary[letter] + "\033[0m")
    else:
        v.append(letter)

print("".join(v))