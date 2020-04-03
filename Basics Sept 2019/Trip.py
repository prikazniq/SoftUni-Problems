budget = float(input())
season = input()

if budget <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        budget = budget - (budget * 0.7)
    elif season == "winter":
        budget = budget - (budget * 0.3)
elif 100 < budget <= 1000:
    print("Somewhere in Balkans")
    if season == "summer":
        budget = budget - (budget * 0.6)
    elif season == "winter":
        budget = budget - (budget * 0.2)
elif budget > 1000:
    print("Somewhere in Europe")
    if season == "summer":
        budget = budget - (budget * 0.1)
    elif season == "winter":
        budget = budget - (budget * 0.1)

if season == "winter" or budget > 1000:
    print(f"Hotel - {budget:.2f}")
elif season == "summer":
    print(f"Camp - {budget:.2f}")