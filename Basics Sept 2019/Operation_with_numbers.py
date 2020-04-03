num1 = int(input())
num2 = int(input())
equal = 0
operator = input()

if operator == "+":
    equal = num1 + num2
    if equal % 2 == 0:
        print(f"{num1} {operator} {num2} = {equal} - even")
    else:
        print(f"{num1} {operator} {num2} = {equal} - odd")

if operator == "-":
    equal = num1 - num2
    if equal % 2 == 0:
        print(f"{num1} {operator} {num2} = {equal} - even")
    else:
        print(f"{num1} {operator} {num2} = {equal} - odd")

if operator == "*":
    equal = num1 * num2
    if equal % 2 == 0:
        print(f"{num1} {operator} {num2} = {equal} - even")
    else:
        print(f"{num1} {operator} {num2} = {equal} - odd")

if operator == "/":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        equal = num1 / num2
        print(f"{num1} {operator} {num2} = {equal:.2f}")

if operator == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        equal = num1 % num2
        print(f"{num1} {operator} {num2} = {equal}")
