flower = input()
quantity = int(input())
budget = int(input())
total = 0
after_discount = 0

if flower == "Roses":
    if quantity > 80:
        discount = 10
        total = (5 * quantity) - ((discount / 100) * 5 * quantity )
        after_discount = budget - total
    else:
        total = budget - (5 * quantity)
        after_discount = total

if flower == "Dahlias":
    if quantity > 90:
        discount = 15
        total = (3.8 * quantity) - ((discount / 100) * 3.8 * quantity)
        after_discount = budget - total
    else:
        total = budget - (3.8 * quantity)
        after_discount = total

if flower == "Tulips":
    if quantity > 80:
        discount = 15
        total = (2.8 * quantity) - ((discount / 100) * 2.8 * quantity)
        after_discount = budget - total
    else:
        total = budget - (2.8 * quantity)
        after_discount = total

if flower == "Narcissus":
    if quantity < 120:
        discount = 15
        total = (3 * quantity) + ((discount / 100) * 3 * quantity)
        after_discount = budget - total
    else:
        total = budget - (3 * quantity)
        after_discount = total

if flower == "Gladiolus":
    if quantity < 80:
        discount = 20
        total = ((2.5 * quantity) + ((discount / 100) * 2.5 * quantity))
        after_discount = budget - total
    else:
        total = budget - (2.5 * quantity)
        after_discount = total

if after_discount < 0:
    print(f"Not enough money, you need {after_discount * -1:.2f} leva more.")
elif after_discount >= 0:
    print(f"Hey, you have a great garden with {quantity:.0f} {flower} and {after_discount:.2f} leva left.")