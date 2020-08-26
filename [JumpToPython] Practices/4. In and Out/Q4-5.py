# File Read/Write Problem
# First Code = Print Nothing
# Second Code = Print "You need Python"

f1 = open("C:/doit/q4-5.txt", 'w')
f1.write("Life is too short")
# f1.close() << Without this, f2 opens an empty file.

f2 = open("C:/doit/q4-5.txt", 'r')
print(f2.read())

'''
with open("C:/doit/q4-5-1.txt", 'w') as f1:
    f1.write("You need Python")

with open("C:/doit/q4-5-1.txt", 'r') as f2:
    print(f2.read())
'''