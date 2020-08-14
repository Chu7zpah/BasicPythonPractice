# Sum Multiples of 3 in range of 1 to 1,000
# Using While Statement

num = sum = 0

while num <= 1000:
    num = num + 1
    if num % 3 == 0:    # Multiples of 3
        sum += num

print("Result:", sum)
