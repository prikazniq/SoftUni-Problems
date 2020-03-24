# goods_list = input().split()
# result = {}
#
# for i in range(0, len(goods_list), 2):
#     key = goods_list[i]
#     value = goods_list[i + 1]
#     result[key] = int(value)
#
# print(result)
# ------------------------------------------------------------
# in_stock = input().split()
# search = input().split()
# fridge = {}
#
# for i in range(0, len(in_stock), 2):
#     key = in_stock[i]
#     value = in_stock[i + 1]
#     fridge[key] = int(value)
#
# for i in search:
#     if i in fridge:
#         print(f"We have {fridge[i]} of {i} left")
#     else:
#         print(f"Sorry, we don't have {i}")

# ----------------------------------------------------------------------
# products_dict = {}
#
# while True:
#     command = input().split(": ")
#     product = command[0]
#     if command[0] == "statistics":
#         print("Products in stock:")
#         for i in products_dict:
#             print(f"- {i}: {products_dict[i]}")
#         print(f"Total Products: {len(products_dict)}")
#         print(f"Total Quantity: {sum(products_dict.values())} ")
#         break
#     quantity = int(command[1])
#     key = product
#     value = quantity
#     if key in products_dict:
#         products_dict[key] += value
#     else:
#         products_dict[key] = value

# -----------------------------------------------------------------------
#
# sequence = input().split()
# sequence_dict = {}
#
# for i in sequence:
#     key = i.lower()
#     if key in sequence_dict:
#         sequence_dict[key] += 1
#         continue
#     sequence_dict[key] = 1
#
# for j in sequence_dict:
#     if sequence_dict[j] % 2 != 0:
#         print(j, end=" ")
# ----------------------------------------------------------------------------

# count_of_pairs = int(input())
# dictionary = {}
#
# for i in range(count_of_pairs):
#     key = input()
#     if key in dictionary:
#         value = input()
#         dictionary[key] += f", {value}"
#         continue
#     value = input()
#     dictionary[key] = value
#
# for i in dictionary:
#     print(f"{i} - {dictionary[i]}")
