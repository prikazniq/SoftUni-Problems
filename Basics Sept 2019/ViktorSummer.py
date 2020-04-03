temp = int(input())
time_of_day = input().lower()

if 10 <= temp <= 18:
    if time_of_day == "morning":
        outfit = str("Sweatshirt")
        shoes = str("Sneakers")
    elif time_of_day == "afternoon":
        outfit = str("Shirt")
        shoes = str("Moccasins")
    elif time_of_day == "evening":
        outfit = str("Shirt")
        shoes = str("Moccasins")

elif 18 <= temp <= 24:
    if time_of_day == "morning":
        outfit = str("Shirt")
        shoes = str("Moccasins")
    elif time_of_day == "afternoon":
        outfit = str("T-Shirt")
        shoes = str("Sandals")
    elif time_of_day == "evening":
        outfit = str("Shirt")
        shoes = str("Moccasins")

elif temp >= 25:
    if time_of_day == "morning":
        outfit = str("T-Shirt")
        shoes = str("Sandals")
    elif time_of_day == "afternoon":
        outfit = str("Swim Suit")
        shoes = str("Barefoot")
    elif time_of_day == "evening":
        outfit = str("Shirt")
        shoes = str("Moccasins")

print(f"It's {temp} degrees, get your {outfit} and {shoes}.")