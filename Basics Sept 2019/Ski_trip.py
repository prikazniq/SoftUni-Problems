days_of_stay = int(input()) - 1
type_of_room = input().lower()
pos_or_not = input().lower()
discount = 0
price = 0
total = 0
total_after = 0

if pos_or_not == "positive":
    if days_of_stay < 10:
        if type_of_room == "room for one person":
            discount = 0
            price = days_of_stay * 18
            total = (price - (price * (discount / 100)))
            total_after = total + (total * 0.25)
            print(f"{total_after:.2f}")
        elif type_of_room == "apartment":
            discount = 30
            price = days_of_stay * 25
            total = price - (price * (discount / 100))
            total_after = total + (total * 0.25)
            print(f"{total_after:.2f}")
        elif type_of_room == "president apartment":
            discount = 10
            price = days_of_stay * 35
            total = price - (price * (discount / 100))
            total_after = total + (total * 0.25)
            print(f"{total_after:.2f}")

    if 10 <= days_of_stay <= 15:
        if type_of_room == "room for one person":
            discount = 0
            price = days_of_stay * 18
            total = price - (price * (discount / 100))
            total_after = total + (total * 0.25)
            print(f"{total_after:.2f}")
        elif type_of_room == "apartment":
            discount = 35
            price = days_of_stay * 25
            total = price - (price * (discount / 100))
            total_after = total + (total * 0.25)
            print(f"{total_after:.2f}")
        elif type_of_room == "president apartment":
            discount = 15
            price = days_of_stay * 35
            total = price - (price * (discount / 100))
            total_after = total + (total * 0.25)
            print(f"{total_after:.2f}")

    if days_of_stay > 15:
        if type_of_room == "room for one person":
            discount = 0
            price = days_of_stay * 18
            total = price - (price * (discount / 100))
            total_after = total + (total * 0.25)
            print(f"{total_after:.2f}")
        elif type_of_room == "apartment":
            discount = 50
            price = days_of_stay * 25
            total = price - (price * (discount / 100))
            total_after = total + (total * 0.25)
            print(f"{total_after:.2f}")
        elif type_of_room == "president apartment":
            discount = 20
            price = days_of_stay * 35
            total = price - (price * (discount / 100))
            total_after = total + (total * 0.25)
            print(f"{total_after:.2f}")

if pos_or_not == "negative":
    if days_of_stay < 10:
        if type_of_room == "room for one person":
            discount = 0
            price = days_of_stay * 18
            total = (price - (price * (discount / 100)))
            total_after = (total - (total * 0.10))
            print(f"{total_after:.2f}")
        elif type_of_room == "apartment":
            discount = 30
            price = days_of_stay * 25
            total = price - (price * (discount / 100))
            total_after = (total - (total * 0.10))
            print(f"{total_after:.2f}")
        elif type_of_room == "president apartment":
            discount = 10
            price = days_of_stay * 35
            total = price - (price * (discount / 100))
            total_after = (total - (total * 0.10))
            print(f"{total_after:.2f}")

    if 10 <= days_of_stay <= 15:
        if type_of_room == "room for one person":
            discount = 0
            price = days_of_stay * 18
            total = price - (price * (discount / 100))
            total_after = (total - (total * 0.10))
            print(f"{total_after:.2f}")
        elif type_of_room == "apartment":
            discount = 35
            price = days_of_stay * 25
            total = price - (price * (discount / 100))
            total_after = (total - (total * 0.10))
            print(f"{total_after:.2f}")
        elif type_of_room == "president apartment":
            discount = 15
            price = days_of_stay * 35
            total = price - (price * (discount / 100))
            total_after = (total - (total * 0.10))
            print(f"{total_after:.2f}")

    if days_of_stay > 15:
        if type_of_room == "room for one person":
            discount = 0
            price = days_of_stay * 18
            total = price - (price * (discount / 100))
            total_after = (total - (total * 0.10))
            print(f"{total_after:.2f}")
        elif type_of_room == "apartment":
            discount = 50
            price = days_of_stay * 25
            total = price - (price * (discount / 100))
            total_after = (total - (total * 0.10))
            print(f"{total_after:.2f}")
        elif type_of_room == "president apartment":
            discount = 20
            price = days_of_stay * 35
            total = price - (price * (discount / 100))
            total_after = (total - (total * 0.10))
            print(f"{total_after:.2f}")