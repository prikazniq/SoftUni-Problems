vacation_needed = float(input())
money_available = float(input())
days_passed_count = 0
operation_money = 0
spend_counter = 0

while not spend_counter == 5 and money_available < vacation_needed:
    operation = input()
    operation_money = float(input())
    days_passed_count += 1
    if operation == "save":
        money_available += operation_money
        spend_counter = 0
    elif operation == "spend":
        money_available -= operation_money
        spend_counter += 1
        if money_available <= 0:
            money_available = 0


if money_available >= vacation_needed:
    print(f"You saved the money for {days_passed_count} days.")
else:
    print(f"You can't save the money.")
    print(days_passed_count)