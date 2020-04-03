import math

record = float(input())
distance = float(input())
timefor1m = float(input())
slowness = (distance // 15) * 12.5
total = timefor1m * distance + slowness
summ = abs(total - record)

if total >= record:
    print(f"No, he failed! He was {abs(summ):.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total:.2f} seconds.")