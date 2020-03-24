# def smallest(a, b, c):
#     if a < b and a < c:
#         return a
#     if b < a and b < c:
#         return b
#     if c < a and c < b:
#         return c
#
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# print(smallest(a, b, c))
#
# ----------------------------------------------------------------------------
#
#
# def sum_numbers(a, b):
#     return a + b
#
#
# def subtract(c):
#     return c
#
#
# def add_and_subtract(a, b, c):
#     return sum_numbers(a, b) - subtract(c)
#
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# print(add_and_subtract(a, b, c))
#
# ---------------------------------------------------------------------------------
#
#
# def ascii_range(first, sencond):
#     for i in range(ord(first) + 1, ord(sencond)):
#         print(chr(i), end=" ")
#
#
# first = input()
# second = input()
#
# ascii_range(first, second,)
#
# ------------------------------------------------------------------------------------------
#
#
# def odd_even_sum(a):
#     even_sum = 0
#     odd_sum = 0
#     for i in str(a):
#         if int(i) % 2 == 0:
#             even_sum += int(i)
#         else:
#             odd_sum += int(i)
#     print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
#
#
# a = int(input())
#
# odd_even_sum(a)
#
# ----------------------------------------------------------------------------------------------------------

# receive_list = input().split(", ")
#
#
# def palindrome():
#     for i in receive_list:
#         reverse = i[::-1]
#         if i == reverse:
#             print(True)
#         else:
#             print(False)
#
# palindrome()

# ---------------------------------------------------------------------------------------
# passwrd = input()
#
#
# def len_of_password(passwrd):
#     if 6 <= len(passwrd) <= 10:
#         return True
#     else:
#         return False
#
#
# def consist(passwrd):
#     for i in passwrd:
#         if i.isdigit() or i.isalpha():
#             continue
#         else:
#             return False
#     return True
#
#
# def digits(passwrd):
#     digit_count = 0
#     for i in passwrd:
#         if i.isdigit():
#             digit_count += 1
#         else:
#             continue
#     if digit_count >= 2:
#         return True
#
#
# def password(passwrd):
#     if digits(passwrd) and len_of_password(passwrd) and consist(passwrd):
#         print("Password is valid")
#     if not len_of_password(passwrd):
#         print("Password must be between 6 and 10 characters")
#     if not consist(passwrd):
#         print("Password must consist only of letters and digits")
#     if not digits(passwrd):
#         print("Password must have at least 2 digits")
#
#
# password(passwrd)

# ----------------------------------------------------------------------------

#
# def perfect_number(n):
#     for i in range(20):
#         perfect = (2 ** (i-1)) * (2 ** i - 1)
#         if perfect == n:
#             return "We have a perfect number!"
#         else:
#             continue
#     return "It's not so perfect."
#
# n = int(input())
#
# print(perfect_number(n))
#
# --------------------------------------------------------------------

# def loading_bar(n):
#     if n == 100:
#         print("100% Complete!")
#         print("[", end="")
#         print((n // 10) * "%", end="")
#         print("]")
#     else:
#         print(f"{n}% [", end="")
#         print((n // 10) * "%", end="")
#         for i in range((100 - n) // 10):
#             print(".", end="")
#         print("]")
#         print("Still loading...")
#
#
# n = int(input())
#
# loading_bar(n)
# ---------------------------------------------------------------
# import math
#
# def factoial_division(n, d):
#     print(f"{(math.factorial(n)) / math.factorial(d):.2f}" )
#
# n = int(input())
# d = int(input())
#
# factoial_division(n, d)
# --------------------------------------------------------------------

array = input().split()
key = input()
count = int(input())


def exchange(key):
    if key > len(array):
        return "Invalid index"
    else:
        for i in array[:key:-1]:
            array.remove(i)
            array.insert(0, i)
        return array


def max_even_odd(key):
    if key == "odd":
        for i in range(len(array), 0, -1):
            if i % 2 == 0:
                return i
    elif key == "even":
        for i in range(len(array), 0, -1):
            if i % 2 != 0:
                return i


def min_even_odd(key):  # secondary must be implemented
    if key == "odd":
        for i in range(0, len(array)):
            if i % 2 != 0:
                return i
    elif key == "even":
        for i in range(0, len(array)):  # may have problem here later check it
            if i % 3 == 0 and i != 0:
                return i


def first_even_odd(count, key):
    new_list = []
    if count > len(array):
        return "Invalid count"
    if key == "odd":
        for i in array:
            if int(i) % 2 != 0:
                new_list.append(i)
                if count == 1:
                    break
                if count == len(new_list):
                    return new_list
        if len(new_list) == 0:
            return []
        if len(new_list) <= count:
            return new_list
    elif key == "even":
        for i in array:
            if int(i) % 2 == 0:
                new_list.append(i)
                if count == 1:
                    break
                if count == len(new_list):
                    return new_list
        if len(new_list) == 0:
            return []
        if len(new_list) <= count:
            return new_list

def last_even_odd(count, key):
    new_list = []
    if count > len(array):
        return "Invalid count"
    if key == "odd":
        for i in array[::-1]:
            if int(i) % 2 != 0:
                new_list.append(i)
                if count == 1:
                    break
                if count == len(new_list):
                    return new_list
        if len(new_list) == 0:
            return []
        if len(new_list) <= count:
            return new_list
    elif key == "even":
        for i in array[::-1]:
            if int(i) % 2 == 0:
                new_list.append(i)
                if count == 1:
                    break
                if count == len(new_list):
                    return new_list
        if len(new_list) == 0:
            return []
        if len(new_list) <= count:
            return new_list

print(last_even_odd(count, key))
