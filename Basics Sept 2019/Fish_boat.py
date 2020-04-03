budget = int(input())
season = input()
fisherman = int(input())
price = 0
discount = 0
total = 0
sum = 0

if season == "Spring":
    price = 3000
    if fisherman <= 6:
        discount = 10
        if fisherman % 2 == 0:
            discount = discount + 5
    if 7 <= fisherman <= 11:
        discount = 15
        if fisherman % 2 == 0:
            discount = discount + 5
    if fisherman >= 12:
        discount = 25
        if fisherman % 2 == 0:
            discount = discount + 5

if season == "Summer" or season == "Autumn":
    price = 4200
    if fisherman <= 6:
        discount = 10
        if fisherman % 2 == 0 and season == "Summer":
            discount = discount + 5
    if 7 <= fisherman <= 11:
        discount = 15
        if fisherman % 2 == 0 and season == "Summer":
            discount = discount + 5
    if fisherman >= 12:
        discount = 25
        if fisherman % 2 == 0 and season == "Summer":
            discount = discount + 5

if season == "Winter":
    price = 2600
    if fisherman <= 6:
        discount = 10
        if fisherman % 2 == 0:
            discount = discount + 5
    if 7 <= fisherman <= 11:
        discount = 15
        if fisherman % 2 == 0:
            discount = discount + 5
    if fisherman >= 12:
        discount = 25
        if fisherman % 2 == 0:
            discount = discount + 5

total = price - (price * (discount/100))
sum = budget - total

if budget >= total:
    print(f"Yes! You have {sum:.2f} leva left.")
else:
    sum = sum * -1
    print(f"Not enough money! You need {sum:.2f} leva.")