km = float(input())
time_of_day = input().lower()
price = 0
if time_of_day == "day":
    taxi_price = 0.79
elif time_of_day == "night":
    taxi_price = 0.90
else:
    print("Invalid time")

if 0 < km < 20:
    price = km * taxi_price + 0.7
elif 20 < km < 100:
    price = km * 0.09
elif km > 100:
    price = km * 0.06
print(price)