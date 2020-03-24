# raw_info = input().split()
# d = {}
#
# for word in raw_info:
#     for letter in word:
#         if letter in d:
#             d[letter] += 1
#         else:
#             d[letter] = 1
#
# for i in d.keys():
#     print(f"{i} -> {d[i]}")
#
# -------------------------------------------------------------
# d = {}
# counter = 0
#
# while True:
#     command = input()
#     if command == "stop":
#         break
#     if counter % 2 == 0:
#         key = command
#     else:
#         value = command
#         if key in d:
#             d[key] += int(value)
#         else:
#             d[key] = int(value)
#     counter += 1
#
# for i in d.keys():
#     print(f"{i} -> {d[i]}")

# ---------------------------------------------------------------------
# key_materials = input().split()
# useful = {"fragments": 0,
#           "motes": 0,
#           "shards": 0
#           }
# junk = {}
# item_crafted = True
#
# while item_crafted:
#     for i in range(0, len(key_materials), 2):
#         key = key_materials[i + 1].lower()
#         value = key_materials[i]
#         if key in useful:
#             useful[key] += int(value)
#             if useful["shards"] >= 250:
#                 print("Shadowmourne obtained!")
#                 useful["shards"] -= 250
#                 item_crafted = False
#                 break
#             elif useful["fragments"] >= 250:
#                 print("Valanyr obtained!")
#                 useful["fragments"] -= 250
#                 item_crafted = False
#                 break
#             elif useful["motes"] >= 250:
#                 print("Dragonwrath obtained!")
#                 useful["motes"] -= 250
#                 item_crafted = False
#                 break
#         else:
#             if key in junk:
#                 junk[key] += int(value)
#             else:
#                 junk[key] = int(value)
#     if item_crafted:
#         key_materials = input().split()
#
# for item, quantity in (sorted(useful.items(), key=lambda x: (-x[1], x[0]))):
#     print(f"{item}: {quantity}")
#
# for item, quantity in (sorted(junk.items())):
#     print(f"{item}: {quantity}")

# --------------------------------------------------------------------------
# item_quantity = {}
# item_value = {}
# total = item_quantity.update(item_value)
#
# while True:
#     raw_data = input().split()
#     if raw_data[0] == "buy":
#         for j in item_value:
#             print(f"{j} -> {item_quantity[j] * item_value[j]:.2f}")
#         break
#     for i in range(0, len(raw_data), 3):
#         key = raw_data[i]
#         value = float(raw_data[i + 1])
#         quantity = int(raw_data[i + 2])
#         if key in item_quantity:
#             item_quantity[key] += quantity
#             item_value[key] = value
#         else:
#             item_quantity[key] = quantity
#             item_value[key] = value
# -------------------------------------------------------------------------
#
# number_of_commands = int(input())
# database = {}
#
# for i in range(number_of_commands):
#     command = input().split()
#     user = command[1]
#     if command[0] == "register":
#         license_plate = command[2]
#         if user in database:
#             print(f"ERROR: already registered with plate number {license_plate}")
#         else:
#             print(f"{user} registered {license_plate} successfully")
#             database[user] = license_plate
#     elif command[0] == "unregister":
#         if user in database:
#             print(f"{user} unregistered successfully")
#             del database[user]
#         else:
#             print(f"ERROR: user {user} not found")
#
# for i in database:
#     print(f"{i} => {database[i]}")
# ---------------------------------------------------------------------
# students = {}
# courses = {}
#
# while True:
#     raw_data = input().split(" : ")
#     if raw_data[0] == "end":
#         break
#     course = raw_data[0]
#     student = raw_data[1]
#     # students[course] = student
#     if course in courses:
#         courses[course] += 1
#     else:
#         courses[course] = 1
#     if course in students:
#         students[course] += f",{student}"
#     else:
#         students[course] = student
#
# for course, participants in sorted(courses.items(), key=lambda x: x[1], reverse=True):
#     print(f"{course}: {int(participants)}")
#     for i in sorted(students[course].split(',')):
#         print(f"-- {i}")
# -----------------------------------------------------------------------
#
# pairs = int(input())
# grades = {}
# average = []
#
# for i in range(pairs):
#     name = input()
#     grade = average.append(float(input()))
#     if name in grades:
#         grades[name] += average
#         average = []
#     else:
#         grades[name] = average
#         average = []
#
# for k, v in sorted(grades.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True):
#     if sum(v) / len(v) >= 4.5:
#         print(f"{k} -> {sum(v) / len(v):.2f}")

# ---------------------------------------------------------------------------

# companies = {}
# id_track = []
#
# while True:
#     command = input().split(" -> ")
#     if command[0] == "End":
#         break
#     company = command[0]
#     id_number = command[1]
#     if company in companies:
#         if id_number not in id_track:
#             companies[company] += f" {id_number}"
#             id_track.append(id_number)
#     else:
#         companies[company] = id_number
#         id_track.append(id_number)
#
# for company, id_number in sorted(companies.items()):
#     print(f"{company}")
#     for i in companies[company].split():
#         print(f"-- {i}")
