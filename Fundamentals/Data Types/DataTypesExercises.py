# import math
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# total = math.floor((a + b) / c)
# total *= d
# print(total)
#
#  ----------------------------------------------------------------------------
#
# a = input()
# b = input()
# c = input()
#
# print(a + b + c)
#
# ---------------------------------------------------------------------------------------
#
# n = int(input())
# p = int(input())
# counter = 0
#
# while n > 0:
#     n -= p
#     counter += 1
#
# print(counter)
#
# ------------------------------------------------------------------------------------------
#
# interval = int(input())
# total = 0
#
# for i in range(interval):
#     next_char = input()
#     total += ord(next_char)
#
# print(f"The sum equals: {total}")

# ----------------------------------------------------------------------------

# start = int(input())
# final = int(input())
#
# for i in range(start, final + 1):
#     print(chr(i), end=" ")

# -----------------------------------------------------------------------------------
#
# n = int(input())
#
# for i in range(0, n):
#     for j in range(0, n):
#         for k in range(0, n):
#             print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")
#
#
# -------------------------------------------------------------------------------------

#
# lines = int(input())
# capacity = 255
# current = 0
#
# for i in range(lines):
#     pour = int(input())
#     if current + pour <= capacity:
#         current += pour
#     else:
#         print("Insufficient capacity!")
#
# print(current)
#
# ----------------------------------------------------------------------------------
# import math
#
# party_size = int(input())
# days = int(input())
# coins = 0
#
# for i in range(1, days + 1):
#     if i % 10 == 0:
#         party_size -= 2
#     if i % 15 == 0:
#         party_size += 5
#     coins += 50 - (2 * party_size)
#     if i % 3 == 0:
#         coins -= 3 * party_size
#     if i % 5 == 0:
#         coins += 20 * party_size
#         if i % 3 == 0:
#             coins -= 2 * party_size
#
# print(f"{party_size} companions received {math.floor(coins/party_size)} coins each.")
#
#  ----------------------------------------------------------------------------------------------
#
# import sys
#
# number_of_snowballs = int(input())
# max = sys.maxsize * -1
#
# for i in range(number_of_snowballs):
#     snowball_snow = int(input())
#     snowball_time = int(input())
#     snowball_quality = int(input())
#     formula = (snowball_snow / snowball_time) ** snowball_quality
#     if formula > max:
#         snow = snowball_snow
#         time = snowball_time
#         quality = snowball_quality
#         max = formula
#
# print(f"{snow:.0f} : {time:.0f} = {max:.0f} ({quality:.0f})")
#
# ----------------------------------------------------------------------------------------------------------

# lost = int(input())
# helmet = float(input())
# sword = float(input())
# shield = float(input())
# armor = float(input())
# counter_armor = 0
# counter_shield = 0
# counter_sword = 0
# counter_helmet = 0
#
# for i in range(1, lost+1):
#     if i % 3 == 0 and i % 2 == 0:
#         counter_shield += 1
#         if counter_shield % 2 == 0:
#             counter_armor += 1
#     if i % 2 == 0:
#         counter_helmet += 1
#     if i % 3 == 0:
#         counter_sword += 1
#
#
# expenses = (counter_armor * armor) + (counter_shield * shield) + (counter_sword * sword) + (counter_helmet * helmet)
#
# print(f"Gladiator expenses: {expenses:.2f} aureus")
