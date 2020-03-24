# line_of_text = input().split(", ")
#
# for word in line_of_text:
#     if 3 <= len(word) <= 16:
#         if word.isalnum() or "-" in word or "_" in word:
#             print(word)
# -------------------------------------------------------------------
#
# two_strings = input().split()
# token1 = two_strings[0]
# token2 = two_strings[1]
# total = 0
# life_cycle = 0
#
# if len(token1) > len(token2):
#     life_cycle = token1
# else:
#     life_cycle = token2
#
# for i in range(len(life_cycle)):
#     if i >= len(token2):
#         total += ord(token1[i])
#         continue
#     elif i >= len(token1):
#         total += ord(token2[i])
#         continue
#     else:
#         total += ord(token1[i]) * ord(token2[i])
#
# print(total)

# -----------------------------------------------------------------------
# directory = input().split("\\")
# file = directory[-1].split(".")
# name = file[0]
# extension = file[1]
#
# print(f"File name: {name}")
# print(f"File extension: {extension}")

# ------------------------------------------------------------------------

# encrypt_this = input()
# encrypted = ""
#
# for letter in encrypt_this:
#     encrypted += chr(ord(letter) + 3)
#
# print(encrypted)
# ----------------------------------------------------------------------

# text = input()
#
# for i in range(len(text)):
#     if text[i] == ":":
#         if text[i + 1] != " ":
#             print(f":{text[i + 1]}")
# -------------------------------------------------------------------------
# text = input()
# sol = ""
#
# for i in range(len(text)):
#     if i == len(text)-1:
#         print(text[i])
#         continue
#     if i + 1 < len(text):
#         if text[i] != text[i + 1]:
#             print(text[i], end="")

# --------------------------------------------------------------------------------
#
# string_to_explode = input()
# power = 0
# i = 0
#
# while i < len(string_to_explode):
#     ch = string_to_explode[i]
#
#     if ch == ">":
#         power += int(string_to_explode[i + 1])
#     elif power > 0:
#         string_to_explode = string_to_explode[:i] + string_to_explode[i + 1:]
#         i -= 1
#         power -= 1
#
#     i += 1
#
# print(string_to_explode)

# -------------------------------------------------------------------

