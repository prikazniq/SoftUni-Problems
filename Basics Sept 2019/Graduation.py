name = input()
level = 1
grade_total = 0
average = 0

while level <= 12:
    grade = float(input())

    if grade >= 4:
        level += 1
        grade_total += grade

print(f"{name} graduated. Average grade: {grade_total / 12:.2f}")