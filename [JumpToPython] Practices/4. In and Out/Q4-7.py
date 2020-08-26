# Replacing Java to Python Program

# Making a input file
with open("C:/doit/q4-7.txt", 'w') as f:
    f.write("Life is too short\n")
    f.write("you need java\n")

# Replacing Java -> Python
with open("C:/doit/q4-7.txt", 'r') as f2:
    file_contents = f2.read()

with open("C:/doit/q4-7.txt", 'w') as f3:
    f3.write(file_contents.replace("java", 'python'))
