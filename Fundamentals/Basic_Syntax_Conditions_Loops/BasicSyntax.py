# a = int(input())
# b = int(input())
# c = int(input())
#
# if a > b and a > c:
#     print(a)
# elif b > a and b >c:
#     print(b)
# else:
#     print(c)
#
# num = float(input())
#
# if num == 0:
#     print("zero")
#
# if -1 < num < 1:
#     print("small", end=" ")
#     if -1 < num < 0:
#         print("negative")
#     else:
#         print("positive")
#
# if num > 1:
#     if num > 1000000:
#         print("large positive")
#     else:
#         print("positive")
# elif num < -1:
#     if num < -1000000:
#         print("large negative")
#     else:
#         print("negative")

# word = input()
# reversed_word = ""
# for i in range(len(word) - 1, -1, -1):
#     reversed_word += word[i]
# print(reversed_word)

# a = float(input())
#
# while a > 100 or a < 1:
#     a = float(input())
#
# print(f"The number {a} is between 1 and 100")

# num = int(input())
# a = "*"
#
# for i in range(1, num+1):
#     for j in range(0, i):
#         print("*", end="")
#     print()
# for i in range(num -1, 0, -1):
#     for j in range(0, i):
#         print("*", end="")
#     print()