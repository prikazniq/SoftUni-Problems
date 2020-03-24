# name = input()
# if name == "Johnny":
#     print(f"Hello, my love!")
# else:
#     print(f"Hello, {name}!")

# ---------------------------------------------------

# age = int(input())
# if age <= 14:
#     print("drink toddy")
# elif 14 < age <= 18:
#     print("drink coke")
# elif 18 < age <= 21:
#     print("drink beer")
# else:
#     print("drink whisky")

# -------------------------------------------------------

# num = int(input())
#
# if num == 88:
#     print("Leo finally won the Oscar! Leo is happy")
# elif num == 86:
#     print("Not even for Wolf of Wall Street?!")
# elif num < 88 and num != 86:
#     print("When will you give Leo an Oscar?")
# else:
#     print("Leo got one already!")

# ----------------------------------------------------------

# thing = input()
#
# for i in (thing):
#     print(i * 2, end="")

# ------------------------------------------------------------

# counter = int(input())
#
# for i in range(1, counter + 1):
#     print(f"{i} sheep...", end="")

# -------------------------------------------------------------

# year = (input())
# year_as_int = int(year) + 1
# year = str(year_as_int)
#
# while True:
#     symbol_count = len(year)
#     unique_symbol = len(set(year))
#     if symbol_count == unique_symbol:
#         break
#     else:
#         year_as_int += 1
#         year = str(year_as_int)
#
# print(year)

# ---------------------------------------------------------------

# divisor = int(input())
# bound = int(input())
# n = bound
#
# while True:
#     if bound >= n > 0 and n % divisor == 0:
#         break
#     else:
#         n -= 1
#         continue
# print(n)

# -------------------------------------------------------------------

# 0first_string = input()
# second_string = input()
#
# for i in range(len(first_string)):
#     if first_string[i] != second_string[i]:
#         for second_string_index in range(0, i+1):
#             print(second_string[second_string_index], end="")
#
#         for str_one_index in range(i + 1, len(first_string)):
#             print(first_string[str_one_index], end="")
#
#         print()

# ----------------------------------------------------------------------

# budget = float(input())
# flour = float(input())
# egg_price = flour * 0.75
# milk_litre_price = flour * 1.25
# milk_needed = milk_litre_price * 0.25
# cozonac = flour + egg_price + milk_needed
# cozonac_counter = 0
# colored_eggs = 0
#
#
# while budget - cozonac > 0:
#     budget -= cozonac
#     cozonac_counter += 1
#     if cozonac_counter % 3 == 0:
#         colored_eggs += 3
#         colored_eggs -= (cozonac_counter - 2)
#     elif cozonac_counter % 1 == 0:
#         colored_eggs += 3
#
# print(f"You made {cozonac_counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

# ----------------------------------------------------------------------------------------------------------------

# quantity = int(input())
# days = int(input())
#
# ornament = 2
# tree_skirt = 5
# tree_garlands = 3
# tree_lights = 15
#
# christmas_spirit = 0
# cost = 0
#
# for i in range(1, days + 1):
#     if i % 11 == 0:
#         quantity += 2
#     if i % 2 == 0:
#         cost += ornament * quantity
#         christmas_spirit += 5
#     if i % 3 == 0:
#         cost += (tree_skirt * quantity) + (tree_garlands * quantity)
#         christmas_spirit += 13
#     if i % 5 == 0:
#         cost += tree_lights * quantity
#         christmas_spirit += 17
#         if i % 3 == 0:
#             christmas_spirit += 30
#     if i % 10 == 0:
#         christmas_spirit -= 20
#         cost += tree_lights + tree_garlands + tree_skirt
#         if i == days:
#             christmas_spirit -= 30
#
# print(f"Total cost: {cost}")
# print(f"Total spirit: {christmas_spirit}")

# -------------------------------------------------------------------------

