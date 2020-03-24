import math

exp_needed = float(input())
count_of_battles = int(input())
counter = 0
total = 0

for i in range(1, count_of_battles + 1):
    battle = int(input())
    counter += 1
    if i % 3 == 0:
        total += math.ceil(battle * 1.15)
    elif i % 5 == 0:
        total += (math.ceil(battle * 0.9))
    else:
        total += battle
    if total >= exp_needed:
        break

if total >= exp_needed:
    print(f"Player successfully collected his needed experience for {counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {exp_needed - total:.2f} more needed.")
# -----------------------------------------------------------------------------------------------

# friends_list = input().split(", ")
# blacklisted_counter = 0
# lost_counter = 0
#
# while True:
#     command = input().split()
#     if command[0] == "Report":
#         break
#     token_1 = command[0]
#     token_2 = command[1]
#     if token_1 == "Blacklist":
#         if token_2 in friends_list:
#             friends_list.insert(friends_list.index(token_2), "Blacklisted")
#             friends_list.remove(token_2)
#             print(f"{token_2} was blacklisted.")
#             blacklisted_counter += 1
#         else:
#             print(f"{token_2} was not found.")
#     elif token_1 == "Error":
#         if friends_list[int(token_2)] == "Blacklisted" or friends_list[int(token_2)] == "Lost":
#             continue
#         else:
#             print(f"{friends_list[int(token_2)]} was lost due to an error.")
#             friends_list[int(token_2)] = "Lost"
#             lost_counter +=1
#     elif token_1 == "Change":
#         token_3 = command[2]
#         if int(token_2) < len(friends_list):
#             print(f"{friends_list[int(token_2)]} changed his username to {token_3}. ")
#             friends_list[int(token_2)] = token_3
#         else:
#             continue
#
#
# print(f"Blacklisted names: {blacklisted_counter} ")
# print(f"Lost names: {lost_counter} ")
# for i in friends_list:
#     print(i, end=" ")
# ----------------------------------------------------------------------

# tanks_owned = input().split(", ")
# loops = int(input())
#
#
# for i in range(loops):
#     command = input().split(", ")
#     token_1 = command[0]
#     token_2 = command[1]
#     if token_1 == "Add":
#         if token_2 in tanks_owned:
#             print("Tank is already bought")
#         else:
#             print("Tank successfully bought")
#             tanks_owned.append(token_2)
#     elif token_1 == "Remove":
#         if token_2 in tanks_owned:
#             print("Tank successfully sold")
#             tanks_owned.remove(token_2)
#         else:
#             print("Tank not found")
#     elif token_1 == "Remove At":
#         if int(token_2) < len(tanks_owned):
#             tanks_owned.remove(tanks_owned[int(token_2)])
#             print("Tank successfully sold")
#         else:
#             print("Index out of range")
#     elif token_1 == "Insert":
#         token_3 = command[2]
#         if int(token_2) > len(tanks_owned):
#             print("Index out of range")
#         elif token_3 in tanks_owned:
#             print("Tank is already bought")
#         elif token_3 not in tanks_owned and int(token_2) < len(tanks_owned):
#             print("Tank successfully bought")
#             tanks_owned.insert(int(token_2), token_3)
#
# print(", ".join(tanks_owned))
