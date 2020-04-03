food_money = float(input())
souvenir_money = float(input())
hotel_price = float(input())
total_money = 0

fuel_money = (420/100 * 7) * 1.85
stay_money = (3 * food_money) + (3 * souvenir_money)
hotel_money_1st = hotel_price * 0.9
hotel_money_2nd = hotel_price * 0.85
hotel_money_3rd = hotel_price * 0.8
total_money = fuel_money + stay_money + hotel_money_1st + hotel_money_2nd + hotel_money_3rd

print(f"Money needed: {total_money:.2f}")