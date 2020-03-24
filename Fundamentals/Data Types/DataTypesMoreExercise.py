# a = int(input())
# b = int(input())
# c = int(input())
#
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

# -----------------------------------------
# a = int(input())
# b = int(input())
# after = 10
#
# print(f"""Before:
# a = {a}
# b = {b}
# After:
# a = {b}
# b = {a}""")

# --------------------------------------------------------------
#
# num = int(input())
#
# if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
#     print(False)
# elif num / num == 1 and num / 1 == num:
#     print(True)
#
# -----------------------------------------------------------------------
# key = int(input())
# n_number_of_char = int(input())
#
# for i in range(n_number_of_char):
#     char = input()
#     print(chr(ord(char) + key), end="")
#
# ---------------------------------------------------------------------------
#
# n_times = int(input())
# open_counter = 0
# close_counter = 0
# two_open = 0
# same_char = ""
#
# for i in range(n_times):
#     random_char = input()
#     if random_char == "(":
#         open_counter += 1
#     if random_char == ")":
#         close_counter += 1
#     if random_char == same_char:
#         two_open += 1
#     same_char = random_char
#
# if open_counter != close_counter or two_open != 0:
#     print("UNBALANCED")
# else:
#     print("BALANCED")