# number = int(input())
# l = []
#
# for i in range(number):
#     l.append(input())
#
# print(l)

# -------------------------------------------------------------
#
# a = input()
# b = input()
# c = input()
#
# l = [a, b, c]
# print(l[::-1])
#
# ---------------------------------------------------------------

# n = int(input())
# list_pos = []
# list_neg = []
# counter_pos = 0
# sum_neg = 0
#
# for i in range(n):
#     var = int(input())
#     if var >= 0:
#         list_pos.append(var)
#         counter_pos += 1
#     else:
#         list_neg.append(var)
#         sum_neg += var
#
# print(list_pos)
# print(list_neg)
# print(f"Count of positives: {counter_pos}. Sum of negatives: {sum_neg}")
#
# --------------------------------------------------------------------
#
# n = int(input())
# word = input()
# list = []
#
#
# for i in range(n):
#     list.append(input())
#
# print(list)
# print([words for words in list if word in words])
#
# ----------------------------------------------------------------------

# n = int(input())
# l = [int(input()) for _ in range(n)]
# filters = []
# func = input()
#
# for number in l:
#     if func == "even" and number % 2 == 0:
#         filters.append(number)
#     if func == "odd" and number % 2 != 0:
#         filters.append(number)
#     if func == "negative" and number < 0:
#         filters.append(number)
#     if func == "positive" and number >= 0:
#         filters.append(number)
#
# print(filters)