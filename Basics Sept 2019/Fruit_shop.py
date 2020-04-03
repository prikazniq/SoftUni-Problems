fruit = input().lower()
day_of_week = input().lower()
quantity = float(input())
result = 0

if day_of_week == "monday"\
        or day_of_week == "tuesday"\
        or day_of_week == "wednesday"\
        or day_of_week == "thursday"\
        or day_of_week == "friday":
    if fruit == "banana":
        result = (2.50 * quantity)
        print(f"{result:.2f}")
    elif fruit == "apple":
        result = 1.20 * quantity
        print(f"{result:.2f}")
    elif fruit == "orange":
        result = (0.85 * quantity)
        print(f"{result:.2f}")
    elif fruit == "grapefruit":
        result = (1.45 * quantity)
        print(f"{result:.2f}")
    elif fruit == "kiwi":
        result = (2.70 * quantity)
        print(f"{result:.2f}")
    elif fruit == "pineapple":
        result = (5.50 * quantity)
        print(f"{result:.2f}")
    elif fruit == "grapes":
        result = (3.85 * quantity)
        print(f"{result:.2f}")

if day_of_week == "saturday" \
        or day_of_week == "sunday":
    if fruit == "banana":
        result = (2.70 * quantity)
        print(f"{result:.2f}")
    elif fruit == "apple":
        result = (1.25 * quantity)
        print(f"{result:.2f}")
    elif fruit == "orange":
        result = (0.90 * quantity)
        print(f"{result:.2f}")
    elif fruit == "grapefruit":
        result = (1.60 * quantity)
        print(f"{result:.2f}")
    elif fruit == "kiwi":
        result = (3 * quantity)
        print(f"{result:.2f}")
    elif fruit == "pineapple":
        result = (5.60 * quantity)
        print(f"{result:.2f}")
    elif fruit == "grapes":
        result = (4.20 * quantity)
        print(f"{result:.2f}")

if result == 0:
    print("error")