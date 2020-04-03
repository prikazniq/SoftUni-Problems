import math

type_of_sushi = input().lower()
restaurant = input()
servings = int(input())
delivery = input().capitalize()
price = 0
with_delivery = 0

if restaurant != "Sushi Zone" and restaurant != "Sushi Bar" and restaurant != "Asian Pub" and restaurant != "Sushi Time":
    print(f"{restaurant} is invalid restaurant!")

if restaurant == "Sushi Zone":
    if type_of_sushi == "sashimi":
        if delivery == "Y":
            price = 4.99 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 4.99 * servings
    elif type_of_sushi == "maki":
        if delivery == "Y":
            price = 5.29 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 5.29 * servings
    elif type_of_sushi == "uramaki":
        if delivery == "Y":
            price = 5.99 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 5.99 * servings
    elif type_of_sushi == "temaki":
        if delivery == "Y":
            price = 4.29 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 4.29 * servings

elif restaurant == "Sushi Time":
    if type_of_sushi == "sashimi":
        if delivery == "Y":
            price = 5.49 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 5.49 * servings
    elif type_of_sushi == "maki":
        if delivery == "Y":
            price = 4.69 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 4.69 * servings
    elif type_of_sushi == "uramaki":
        if delivery == "Y":
            price = 4.49 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 4.49 * servings
    elif type_of_sushi == "temaki":
        if delivery == "Y":
            price = 5.19 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 5.19 * servings

elif restaurant == "Sushi Bar":
    if type_of_sushi == "sashimi":
        if delivery == "Y":
            price = 5.25 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 5.25 * servings
    elif type_of_sushi == "maki":
        if delivery == "Y":
            price = 5.55 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 5.55 * servings
    elif type_of_sushi == "uramaki":
        if delivery == "Y":
            price = 6.25 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 6.25 * servings
    elif type_of_sushi == "temaki":
        if delivery == "Y":
            price = 4.75 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 4.75 * servings

elif restaurant == "Asian Pub":
    if type_of_sushi == "sashimi":
        if delivery == "Y":
            price = 4.5 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 4.5 * servings
    elif type_of_sushi == "maki":
        if delivery == "Y":
            price = 4.8 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 4.8 * servings
    elif type_of_sushi == "uramaki":
        if delivery == "Y":
            price = 5.5 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 5.5 * servings
    elif type_of_sushi == "temaki":
        if delivery == "Y":
            price = 5.5 * servings
            with_delivery = price + (price * 0.20)
        else:
            price = 5.5 * servings

if with_delivery > 0 and (restaurant == "Sushi Zone" or restaurant == "Sushi Bar" or restaurant == "Asian Pub" or restaurant == "Sushi Time"):
    print(f"Total price: {math.ceil(with_delivery)} lv.")
if delivery == "N" and (restaurant == "Sushi Zone" or restaurant == "Sushi Bar" or restaurant == "Asian Pub" or restaurant == "Sushi Time"):
    print(f"Total price: {math.ceil(price)} lv.")
