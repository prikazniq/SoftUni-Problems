import math

num = int(input())
a = math.floor(num % 10)
b = math.floor(((num / 10) % 10))
c = math.floor(num / 100)

for d in range(1, a+1):
    for e in range(1, b+1):
        for f in range(1, c+1):
            if a * b * c != 0:
                print(f"{d} * {e} * {f} = {d * e * f};")