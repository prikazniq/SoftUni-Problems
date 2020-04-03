# price_of_whiskey = float(input())
# q_of_water = float(input())
# q_of_wine = float(input())
# q_of_champagne = float(input())
# q_of_whiskey = float(input())
#
# champagne_price = price_of_whiskey / 2
# wine_price = champagne_price - (champagne_price * 0.6)
# water_price = champagne_price - (champagne_price * 0.9)
#
# total = (wine_price * q_of_wine) + (water_price * q_of_water) + (q_of_whiskey * price_of_whiskey) + (q_of_champagne * champagne_price)
# print(f"{total:.2f}")

# tshirt_price = float(input())
# obj =  float(input())
#
# shorts_price = tshirt_price - (tshirt_price * 0.25)
# socks_price = shorts_price - (shorts_price * 0.8)
# shoes_price = (shorts_price + tshirt_price) * 2
#
# total = tshirt_price + shorts_price + socks_price + shoes_price
# discount = total - (total * 0.15)
#
# if discount >= obj:
#     print(f"Yes, he will earn the world-cup replica ball!")
#     print(f"His sum is {discount:.2f} lv.")
# else:
#     print(f"No, he will not earn the world-cup replica ball.")
#     print(f"He needs {obj - discount:.2f} lv. more.")


# budget = float(input())
# city = input()
# nights = int(input())
# total = 0
#
# if city == "Cairo":
#     total = 500 * nights + 600
#     if nights <= 4:
#         total -= total * 0.03
#     elif 5 <= nights <= 9:
#         total -= total * 0.05
#     elif 10 <= nights <= 24:
#         total -= total * 0.1
#     elif 25 <= nights <= 49:
#         total -= total * 0.17
#     elif 50 <= nights:
#         total -= total * 0.30
# if city == "Paris":
#     total = 300 * nights + 350
#     if 5 <= nights <= 9:
#         total -= total * 0.07
#     elif 10 <= nights <= 24:
#         total -= total * 0.12
#     elif 25 <= nights <= 49:
#         total -= total * 0.22
#     elif 50 <= nights:
#         total -= total * 0.30
# if city == "Lima":
#     total = 800 * nights + 850
#     if 25 <= nights <= 49:
#         total -= total * 0.19
#     elif 50 <= nights:
#         total -= total * 0.30
# if city == "New York":
#     total = 600 * nights + 650
#     if nights <= 4:
#         total -= total * 0.03
#     elif 5 <= nights <= 9:
#         total -= total * 0.05
#     elif 10 <= nights <= 24:
#         total -= total * 0.12
#     elif 25 <= nights <= 49:
#         total -= total * 0.19
#     elif 50 <= nights:
#         total -= total * 0.30
# if city == "Tokyo":
#     total = 700 * nights+ 700
#     if 10 <= nights <= 24:
#         total -= total * 0.12
#     elif 25 <= nights <= 49:
#         total -= total * 0.17
#     elif 50 <= nights:
#         total -= total * 0.30
#
# if budget > total:
#     print(f"Yes! You have {budget - total:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {total - budget:.2f} leva.")



# name = input()
# played_matches = int(input())
# played_count = 1
# points = 0
# goal_diff = 0
# goal = 0
# goal_rec = 0
#
# while played_count <= played_matches:
#     goals = int(input())
#     goal += goals
#     goals_recieved = int(input())
#     goal_rec += goals_recieved
#     played_count += 1
#     if goals > goals_recieved:
#         points += 3
#         goal_diff += goals - goals_recieved
#     elif goals == goals_recieved:
#         points += 1
#     else:
#         points += 0
#         goal_diff -= goals_recieved - goals
#
# if goal >= goal_rec:
#     print(f"{name} has finished the group phase with {points} points.")
#     print(f"Goal difference: {goal_diff}.")
# else:
#     print(f"{name} has been eliminated from the group phase.")
#     print(f"Goal difference: {goal_diff}.")



# n = int(input())
# m = int(input())
# s = int(input())
#
# for i in reversed(range(n, m+1)):
#     if i % 2 == 0 and i % 3 == 0:
#         if s == i:
#             break
#         print(i, end= " ")




# male = int(input())
# female = int(input())
# max = int(input())
# max_count = 0
#
# for m in range(1, male + 1):
#     for f in range(1, female + 1):
#         max_count += 1
#         if max_count <= max:
#             print(f"({m} <-> {f})", end=" ")
























