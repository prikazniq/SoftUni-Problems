name = input()
level = 1
grade_total = 0
bad_grades_counter = 0

while level <= 12:
    if bad_grades_counter == 2:
        print(f"{name} has been excluded at {level} grade")
        break
    grade = float(input())

    if grade >= 4:
        level += 1
        grade_total += grade
    else:
        bad_grades_counter += 1

if bad_grades_counter < 2:
    print(f"{name} graduated. Average grade: {grade_total / 12:.2f}")