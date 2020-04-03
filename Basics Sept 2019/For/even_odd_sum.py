n = int(input())
evensum = 0
oddsum = 0

for i in range(n):
    x1 = int(input())
    if i % 2 == 0:
        evensum += x1
    else:
        oddsum += x1

if oddsum == evensum:
    print(f"Yes")
    print(f"Sum = {oddsum}")
else:
    print(f"No")
    print(f"Diff = {abs(oddsum - evensum)}")