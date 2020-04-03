singer = int(input())
people_count = 0
people = 0
group_price = 0
total = 0

while people != "The restaurant is full":
    people = input()
    if people == "The restaurant is full":
        break
    else:
        people = int(people)

    people_count += people

    if people < 5:
        group_price = people * 100
    else:
        group_price = people * 70

    total += group_price

if total >= singer:
    print(f"You have {people_count} guests and {total - singer} leva left.")
else:
    print(f"You have {people_count} guests and {total} leva income, but no singer.")
