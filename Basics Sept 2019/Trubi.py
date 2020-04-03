import math

v = float(input())
p1 = float(input())
p2 = float(input())
h = float(input())
water = (p1 + p2) * h
if water <= v:
    print("The pool is {0}% full. Pipe 1: {1}%. Pipe 2: {2}%.".format(
        math.trunc(water / v * 100),
        math.trunc(p1 * h / water * 100),
        math.trunc(p2 * h / water * 100),
          ))
else:
    print("For {0} hours the pool overflows with {1} liters.".format(h, math.trunc(water - v)))
