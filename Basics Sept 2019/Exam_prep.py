failed = int(input())
counter_failed = 0
total_marks = 0
quantity_of_marks = 0


while counter_failed <= failed:
    task = input()
    if task == "Enough" or counter_failed == failed:
        break
    mark_on_task = int(input())
    quantity_of_marks += 1
    prev_task = task
    if mark_on_task >= 2:
        total_marks += mark_on_task
    if mark_on_task <= 4:
        counter_failed += 1


if counter_failed < failed or task == "Enough":
    print(f"Average score: {total_marks / quantity_of_marks:.2f}")
    print(f"Number of problems: {quantity_of_marks}")
    print(f"Last problem: {prev_task}")
else:
    print(f"You need a break, {failed} poor grades.")

failed_limit = int(input())
failed_times = 0
solved_count = 0
grade_total = 0
last_problem = ""
has_failed = True

while failed_times < failed_limit:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grade_total += grade
    solved_count += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {failed_times} poor grades.")
else:
    print(f"Average score: {grade_total / solved_count:.2f}")
    print(f"Number of problems: {solved_count}")
    print(f"Last problem: {last_problem}")