# def data_types(cmd, num):
#     if cmd == "int":
#         return int(num) * 2
#     elif cmd == "real":
#         return (f"{int(num)*1.5:.2f}")
#     elif cmd == "string":
#         return (f"${num}$")
#
# cmd = input()
# num = input()
#
# print(data_types(cmd, num))
#
# -------------------------------------------------------------------------------------------------------
# import math
#
#
# def closest_to_center(x1, y1, x2, y2):
#     answer = []
#     counter = 0
#     if x1 == y1 and counter < 2:
#         answer.append(x1)
#         counter += 1
#     if x2 == y2 and counter < 2:
#         answer.append(x2)
#         counter += 1
#     if x1 == x2 and counter < 2:
#         answer.append(x1)
#         counter += 1
#     if y1 == y2 and counter < 2:
#         answer.append(y1)
#         counter += 1
#     if x1 < x2 and counter < 2:
#         answer.append(x1)
#         counter += 1
#     if x2 < x1:
#         answer.append(x2)
#         counter += 1
#     if y1 < y2 and counter < 2:
#         answer.append(y1)
#         counter += 1
#     if y2 < y1 and counter < 2:
#         answer.append(y2)
#         counter += 1
#
#     return (f"({math.trunc(answer[0])}, {math.trunc(answer[1])})")
#
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
#
# print(closest_to_center(x1, y1, x2, y2))
#
# ---------------------------------------------------------------------------------

num = int(input())
total = 0

for i in range(1, num+1):
    total += (num - 1)

print(total)
