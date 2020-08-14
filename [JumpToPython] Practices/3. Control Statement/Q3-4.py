# Print 1 to 100 using For statement

for num in range(100):
    print("%2d" % (num+1), end=' ')

    if num % 10 == 9:
        print(' ')
