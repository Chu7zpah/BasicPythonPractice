# Odd / Even Number distinguish program using Function

def is_odd(num):
    if num % 2 == 0:
        print("{0} is EVEN Number".format(num))
    else:
        print("{0} is ODD Number".format(num))

    return


numeric = int(input("Enter an Numeric: "))
is_odd(numeric)
