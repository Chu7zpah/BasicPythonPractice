# Caesar Cipher Program (ROT13)
'''
    [Main Problems to solve]
        1. Upper / Lower Case Handling --- (Unsolved)
        2. Other Characters(Numeric, Special ...) Handling --- (Solved)
            >> Using alphabet lists & If statements
'''

alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
plain_text = list(input("Enter Plain Text to Encode(Decode): "))

for letter in plain_text:
    if letter in alphabets:
        print(alphabets[(alphabets.index(letter) + 13) % 26], end='')
    else:
        print(letter, end='')
