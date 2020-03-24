# substrings = input().split(", ")
# unique_words = input()
# answer = []
#
# for i in substrings :
#     if i in unique_words:
#         answer.append(i)
#
# print(answer)

# ----------------------------------------------------------


# numbers = [num for num in input().split()]
# numbers.sort()
# numbers.reverse()
# for i in numbers:
#     print(int(i), end="")

# ------------------------------------------------------------

# version = [int(ver) for ver in input().split(".")]
#
# if version[2] >= 9:
#     version[2] = 0
#     version[1] += 1
#     if version[1] > 9:
#         version[1] = 0
#         version[0] += 1
# else:
#     version[2] += 1
#
#
# print(f"{version[0]}.{version[1]}.{version[2]}")

# ---------------------------------------------------------------

# rooms = int(input())
# check = []
# count = 0
# counter_need = 0
#
# for i in range(1, rooms + 1):
#     check = input().split()
#     x = check[0].count("X")
#     taken = int(check[1])
#     if x > taken:
#         count += x - taken
#     if x < taken:
#         print(f"{abs(x - taken)} more chairs needed in room {i}")
#         counter_need += 1
#     if i == rooms and counter_need <= 0:
#         print(f"Game On, {count} free chairs left")

# ----------------------------------------------------------------------

# n = int(input())
# answer = []
#
# for i in range(1, 11):
#     if 0 < n < 2 * (i ** 2):
#         answer.append(n)
#         break
#     if n > 0:
#         n -= 2 * (i ** 2)
#         answer.append(2 * (i ** 2))
#
# print(answer)

# ------------------------------------------------------------------
# import math
#
# def roundup(max_value):
#     return int(math.ceil(max_value / 10)) * 10
#
# numbers = [int(num) for num in input().split(", ")]
# max_value = max(numbers)
#
# for i in range(10, roundup(max_value) + 1, 10):
#     x = [int(num) for num in numbers if num <= i]
#     for j in x:
#         numbers.remove(j)
#     print(f"Group of {i}'s: {x}")

# -------------------------------------------------------------------------
def find_numbers(num):
    arr = list(num)
    num_str = ""
    while True:
        if not arr[0].isdigit():
            break
        num_str += arr[0]
        arr.pop(0)
    num = int(num_str)
    arr.insert(0, chr(num))
    return "".join(arr)


def switch_letters(num):
    result = ""
    list_chars = list(num)
    list_chars[1], list_chars[-1] = list_chars[-1], list_chars[1]
    return "".join(list_chars)


def decrypt(num):
    num = find_numbers(num)
    num = switch_letters(num)
    return num


secret_message = input().split()

words = [decrypt(num) for num in secret_message]
print(" ".join(words))
