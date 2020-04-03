num = int(input())
total = 0
afterbonus = 0
if num <= 100:
    total = num + 5
elif 100 < num <= 1000:
    total = num + (num * 0.20)
elif num > 1000:
    total = num + (num * 0.10)
if num % 2 == 0:
    total = total + 1
elif num % 5 == 0:
    total = total + 2
elif num % 2 != 0:
    total = total

print(total - num)
print(total)