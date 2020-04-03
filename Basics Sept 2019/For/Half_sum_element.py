import sys

maxnum = -sys.maxsize
n = int(input())
sum_num = 0

for i in range(n):
    current = int(input())

    if current > maxnum:
        maxnum = current

    sum_num += current

sum_num -= maxnum
if sum_num == maxnum:
    print("Yes")
    print(f"Sum = {sum_num}")
else:
    print("No")
    print(f"Diff = {abs(maxnum - sum_num)}")