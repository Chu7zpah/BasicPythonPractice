# Calculate Average Score using For statement

class_a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0

for score in class_a:
    sum = sum + score

average_score = sum / len(class_a)
print("Average Score:", average_score)