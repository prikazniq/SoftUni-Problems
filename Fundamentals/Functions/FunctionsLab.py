# def is_fail(grade):
#     return 2.00 <= grade <= 2.99
#
#
# def is_poor(grade):
#     return 3.00 <= grade <= 3.49
#
#
# def is_good(grade):
#     return 3.50 <= grade <= 4.49
#
#
# def is_very_good(grade):
#     return 4.50 <= grade <= 5.49
#
#
# def is_excellent(grade):
#     return 5.50 <= grade <= 6
#
#
# def answer(grade):
#     list_of_marks = [
#         [is_fail, "Fail"],
#         [is_poor, "Poor"],
#         [is_good, "Good"],
#         [is_very_good, "Very Good"],
#         [is_excellent, "Excellent"]
#     ]
#     for fn, mark in list_of_marks:
#         if fn(grade):
#             return mark
#
#
# grade = float(input())
#
# print(answer(grade))
#
# -------------------------------------------------------------------------
#
# def multiply(a, b):
#     return a * b
#
#
# def add(a, b):
#     return a + b
#
#
# def divide(a, b):
#     return a // b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def answer(operator):
#     list_of_operators = [
#         ["multiply", multiply],
#         ["add", add],
#         ["divide", divide],
#         ["subtract", subtract],
#     ]
#     for op, fn in list_of_operators:
#         if op == operator:
#             return fn(a, b)
#
# operator = input()
# a = int(input())
# b = int(input())
#
# print(answer(operator))
#
# --------------------------------------------------------------------------
#
# def repeat(info, n):
#     result = ""
#     for i in range(n):
#         result += info
#     return result
#
# info = input()
# n = int(input())
#
# print(repeat(info, n))
#
# -------------------------------------------------------------------

#
# def coffee(quantity):
#     return 1.50 * quantity
#
#
# def water(quantity):
#     return 1 * quantity
#
#
# def coke(quantity):
#     return 1.4 * quantity
#
#
# def snacks(quantity):
#     return 2 * quantity
#
#
# def total(quantity):
#     list_of_products = [
#         ["coffee",coffee],
#         ["water", water],
#         ["coke", coke],
#         ["snacks", snacks]
#     ]
#     for product_get, fn in list_of_products:
#         if product_get == product:
#             return fn(quantity)
#
#
# product = input()
# quantity = int(input())
#
# print(f"{total(quantity):.2f}")

# ------------------------------------------------------------------------------------
#
# def area(a, b):
#     return a * b
#
#
# a = int(input())
# b = int(input())
#
# print(area(a, b))
