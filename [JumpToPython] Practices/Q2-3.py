# Social Serial Number Slicing Program
# Slicing to YYMMDD(Front) and Others(Back)

social_serial_number = input("Enter Social Serial Number: ")
ssn_split = social_serial_number.split("-")
front = ssn_split[0]
back = ssn_split[1]

print("YYMMDD: {}".format(front))
print("Others: {}".format(bacSk))