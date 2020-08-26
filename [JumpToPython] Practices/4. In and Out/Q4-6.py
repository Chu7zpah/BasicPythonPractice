# Write User's Input to File
# If File already exist, Then add, do not Overwrite

with open("c:/doit/q4-6.txt", 'a') as f:
    f.write(input("Enter User's Input: "))
    f.write("\n")
