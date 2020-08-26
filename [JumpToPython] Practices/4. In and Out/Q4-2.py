# Average Calculator
# No Input details(# of inputs)
# Using Function
'''
def average_calculate(nums):
    sum = 0
    for i in nums:
        sum += float(i)

    return sum/len(nums)


num_lists = input("Enter numbers to calculate(distinguished by ' '): ").split()
average = average_calculate(num_lists)
print(average)

'''

# Using * argument
def average_calculate(*nums):
    sum = 0
    for i in nums:
        sum += i

    average = sum/len(nums)
    return average


result = average_calculate(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)
