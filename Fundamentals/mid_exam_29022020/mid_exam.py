# import sys
# import math
#
# student_count = int(input())
# lecture_count = int(input())
# intial_bounus = int(input())
# max_bonus = -sys.maxsize
# max_attend = -sys.maxsize
#
# if student_count <= 0 or lecture_count <= 0:
#     max_attend = 0
#     max_bonus = 0
#
# for i in range(student_count):
#     student_attend = int(input())
#     total = math.ceil(student_attend / lecture_count * (5 + intial_bounus))
#     if total >= max_bonus:
#         max_bonus = total
#     if student_attend >= max_attend:
#         max_attend = student_attend
#         if max_attend >= lecture_count:
#             max_attend = lecture_count
#
# print(f"Max Bonus: {max_bonus}.")
# print(f"The student has attended {max_attend} lectures.")
+
# -------------------------------------------------------------------------
# hp = 100
# bitcoins = 0
# room_counter = 0
#
# rooms_to_explore = input().split("|")
# for i in rooms_to_explore:
#     room_counter += 1
#     command = i.split()
#     if command[0] == "potion":
#         if hp + int(command[1]) >= 100:
#             print(f"You healed for {100 - hp} hp.")
#             hp += 100 - hp
#             print(f"Current health: {hp} hp.")
#         else:
#             hp += int(command[1])
#             print(f"You healed for {command[1]} hp.")
#             print(f"Current health: {hp} hp.")
#         if hp > 100:
#             hp = 100
#     elif command[0] == "chest":
#         bitcoins += int(command[1])
#         print(f"You found {command[1]} bitcoins.")
#     else:
#         hp -= int(command[1])
#         if hp > 0:
#             print(f"You slayed {command[0]}.")
#         else:
#             print(f"You died! Killed by {command[0]}.")
#             print(f"Best room: {room_counter}")
#             break
#
# if hp > 0:
#     print("You've made it!")
#     print(f"Bitcoins: {bitcoins}")
#     print(f"Health: {hp}")
# -------------------------------------------------------------------

# journal_items = input().split(", ")
#
# while True:
#     command = input().split(" - ")
#     if command[0] == "Craft!":
#         print(", ".join(journal_items))
#         break
#     if command[0] == "Collect":
#         if command[1] in journal_items:
#             pass
#         else:
#             journal_items.append(command[1])
#     elif command[0] == "Drop":
#         if command[1] in journal_items:
#             journal_items.remove(command[1])
#     elif command[0] == "Combine Items":
#         item_check = command[1].split(":")
#         if item_check[0] in journal_items:
#             journal_items.insert(journal_items.index(item_check[0]) + 1, item_check[1])
#     elif command[0] == "Renew":
#         if command[1] in journal_items:
#             journal_items.remove(command[1])
#             journal_items.append(command[1])
