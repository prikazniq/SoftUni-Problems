# vagoons = int(input()) * [0]
#
# command = input().split()
# while command[0] != "End":
#     if command[0] == "add":
#         vagoons[-1] += int(command[1])
#     elif command[0] == "insert":
#         vagoons[int(command[1])] += int(command[2])
#     elif command[0] == "leave":
#         vagoons[int(command[1])] -= int(command[2])
#     command = input().split()
#
# print(vagoons)

# -----------------------------------------------------
# list = [0] * 11
#
# while True:
#     command = input().split("-")
#     if "End" in command:
#         break
#     importance = int(command[0])
#     task = command[1]
#     list.insert(importance, task)
# while 0 in list:
#     list.remove(0)
#
# print(list)
#
# 80/100
#
# -------------------------------------------------------

# pali = input().split()
# search = input()
# count = 0
# answer_list = []
#
# for i in pali:
#     if i[::1] == i[::-1]:
#         if search == i:
#             count += 1
#         answer_list.append(i)
#
# print(f"{answer_list} \n Found palindrome {count} times")

# -----------------------------------------------------------------

# num = input().split(",")
# answer = []
# counter = 0
#
# for i in num:
#     if int(i) % 2 == 0:
#         answer.append(counter)
#         counter += 1
#     else:
#         counter += 1
#         continue
#
# print(answer)

# ----------------------------------------------------------

# employee_happiness = [int(happy) for happy in input().split()]
# happiness_improvement = int(input())
# improvement_fn = list(map(lambda h: h * happiness_improvement, employee_happiness))
# filtered = list(filter(lambda x: x >= (sum(improvement_fn) / len(employee_happiness)), improvement_fn))
#
# if len(filtered) >= len(improvement_fn) // 2:
#     print(f"Score: {len(filtered)}/{len(improvement_fn)}. Employees are happy!")
# else:
#     print(f"Score: {len(filtered)}/{len(improvement_fn)}. Employees are not happy!")
