import math

shape = input().lower()
a = 0
b = 0
r = 0
h = 0
perimeter = 0
if shape == ("square"):
    a = float(input())
    perimeter = a * a
    print(f"{perimeter:.3f}")
elif shape == ("rectangle"):
    a = float(input())
    b = float(input())
    perimeter =  a * b
    print(f"{perimeter:.3f}")
elif shape == ("circle"):
    r = float(input())
    perimeter = math.pi*r*r
    print(f"{perimeter:.3f}")
elif shape == ("triangle"):
    a = float(input())
    h = float(input())
    perimeter = (a*h)/2
    print(f"{perimeter:.3f}")