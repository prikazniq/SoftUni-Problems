# inp = input()
# list = []
# x = inp.split()
#
# for i in x:
#     list.append(int(i)*-1)
#
# print(list)
#
# -----------------------------------------------
#
# factor = int(input())
# count = int(input())
#
# list = [i for i in range(factor, factor * count + 1, factor)]
# print(list)
#
#
# ---------------------------------------------------

# team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
# team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
#
# cards = input()
# to_remove = cards.split()
#
# for i in to_remove:
#     if i in team_a:
#         team_a.remove(i)
#     if i in team_b:
#         team_b.remove(i)
#
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
# if len(team_a) < 7 or (len(team_b)) < 7:
#     print("Game was terminated")
#
# ----------------------------------------------------------
#
# num = input()
# divisor = int(input())
# list = num.split(", ")
# answer = []
# sum = 0
# sum_2 = 0
# if len(list) == divisor:
#     for i in list:
#         answer.append(int(i))
# elif len(list) < divisor:
#     for i in list:
#         answer.append(int(i))
#     for j in range(divisor - len(list)):
#         answer.append(0)
# elif len(list) > divisor:
#     for i in list[::divisor]:
#         sum += int(i)
#         list.remove(i)
#     answer.append(sum)
#     for i in list:
#         sum_2 += int(i)
#         list.remove(i)
#     answer.append(sum_2)
#
# print(answer)

# ------------------------------------------------------------------------------------
# num = input()
# divisor = int(input())
# list = num.split(", ")
# answer = []
# summary = 0
#
#
# if len(list) == divisor:
#     for i in list:
#         answer.append(int(i))
# elif len(list) < divisor:
#     for i in list:
#         answer.append(int(i))
#     for j in range(divisor - len(list)):
#         answer.append(0)
# elif len(list) > divisor:
#     for i in range(divisor):
#         summary = 0
#         if i == 0:
#             for j in list[::divisor]:
#                 summary += int(j)
#         else:
#             for j in list[i::divisor]:
#                 summary += int(j)
#         answer.append(summary)
#
# print(answer)

# ------------------------------------------------------------------

# faro = input().split()
# shuff = int(input())
# mid = len(faro) // 2
#
# for i in range(shuff):
#     ans = []
#     for j in range(mid):
#         ans.append(faro[j])
#         ans.append(faro[j + mid])
#     faro = ans
#
# print(ans)

# -------------------------------------------------------------------------

# num = input().split()
# remove = int(input())
# to_numbers = []
#
# for i in num:
#     to_numbers.append(int(i))
#
# for i in range(remove):
#     to_numbers.remove(min(to_numbers))
#
# print(to_numbers)


# ------------------------------------------------------------------------------
# level_of_fire = input().split("#")
# water = int(input())
# effort = 0
# total_fire = 0
# print("Cells:")
#
# for i in level_of_fire:
#     cells = i.split(" = ")
#     if water >= int(cells[1]):
#         if cells[0] == "High" and 81 <= int(cells[1]) <= 125:
#             print(f" - {cells[1]}")
#             water -= int(cells[1])
#             effort += int(cells[1])*0.25
#             total_fire += int(cells[1])
#         if cells[0] == "Medium" and 51 <= int(cells[1]) <= 80:
#             print(f" - {cells[1]}")
#             water -= int(cells[1])
#             effort += int(cells[1]) * 0.25
#             total_fire += int(cells[1])
#         if cells[0] == "Low" and 1 <= int(cells[1]) <= 50:
#             print(f" - {cells[1]}")
#             water -= int(cells[1])
#             effort += int(cells[1]) * 0.25
#             total_fire += int(cells[1])
#
# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {total_fire}")

# --------------------------------------------------------------------------
#
# items = input().split("|")
# budget = int(input())
# new_price = 0
# total = 0
# spent = 0
#
# for i in items:
#     prices = i.split("->")
#     if float(prices[1]) <= budget:
#         if prices[0] == "Clothes" and float(prices[1]) <= 50:
#             budget -= float(prices[1])
#             total += float(prices[1]) + (float(prices[1]) * 0.4)
#             new_price = float(prices[1]) + (float(prices[1]) * 0.4)
#             print(f"{new_price:.2f}", end=" ")
#             spent += float(prices[1])
#         if prices[0] == "Shoes" and float(prices[1]) <= 35:
#             budget -= float(prices[1])
#             total += float(prices[1]) + (float(prices[1]) * 0.4)
#             new_price = float(prices[1]) + (float(prices[1]) * 0.4)
#             print(f"{new_price:.2f}", end=" ")
#             spent += float(prices[1])
#         if prices[0] == "Accessories" and float(prices[1]) <= 20.50:
#             budget -= float(prices[1])
#             total += float(prices[1]) + (float(prices[1]) * 0.4)
#             new_price = float(prices[1]) + (float(prices[1]) * 0.4)
#             print(f"{new_price:.2f}", end=" ")
#             spent += float(prices[1])
#
#
#
# print(f"\nProfit: {(total - spent):.2f}")
#
# if total + budget > 150:
#     print("Hello, France!")
# else:
#     print("Time to go.")
#
# -----------------------------------------------------------------------------------------

energy = 100
coins = 100
events = input().split("|")
counter = 0

for i in events:
    to_do = i.split("-")
    if to_do[0] == "rest":
        energy += int(to_do[1])
        if energy >= 100:
            print(f"You gained 0 energy.")
            energy = 100
        else:
            print(f"You gained {to_do[1]} energy.")
        print(f"Current energy: {energy}.")
    if to_do[0] == "order":
        if energy >= 30:
            energy -= 30
            print(f"You earned {to_do[1]} coins.")
            coins += int(to_do[1])
        else:
            energy += 50
            print("You had to rest!")
    if to_do[0] != "order" and to_do[0] != "rest":
        if coins > int(to_do[1]):
            print(f"You bought {to_do[0]}.")
            coins -= int(to_do[1])
        elif coins < int(to_do[1]):
            print(f"Closed! Cannot afford {to_do[0]}.")
            counter += 1
            break

if counter < 1:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
