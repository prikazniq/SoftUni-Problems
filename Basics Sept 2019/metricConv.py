num = float(input())
ot = input().lower()
kum = input().lower()
if ot == "mm" and kum == "m":
    num = num * 0.001
    print(f"{num:.3f}")
if ot == "m" and kum == "mm":
    num = num * 1000
    print(f"{num:.3f}")
if ot == "cm" and kum == "m":
    num = num * 0.01
    print(f"{num:.3f}")
if ot == "m" and kum == "cm":
    num = num * 100
    print(f"{num:.3f}")
if ot == "cm" and kum == "mm":
    num = num * 10
    print(f"{num:.3f}")
if ot == "mm" and kum == "cm":
    num = num * 0.1
    print(f"{num:.3f}")