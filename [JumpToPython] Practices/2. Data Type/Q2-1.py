# Average Calculating Program

korean = float(input("Score of Korean: "))
english = float(input("Score of English: "))
math = float(input("Score of Math: "))

sum = korean + english + math
average = sum / 3

print("Average Score: {}".format(average))
