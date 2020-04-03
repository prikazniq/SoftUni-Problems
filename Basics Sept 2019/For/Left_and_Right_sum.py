n = int(input())
leftsum = 0
rightsum = 0

for i in range(n * 2):
    x1 = int(input())
    if i < n:
        leftsum += x1
    else:
        rightsum += x1

if leftsum == rightsum:
    print(f"Yes, sum = {leftsum}")
else:
    print(f"No, diff = {abs(leftsum - rightsum)}")