w = int(input())
l = int(input())
area = w*l
total = 0

while area >= total:
    part = input()
    if part == "STOP":
        if area - total > 0:
            print(f"{area - total} pieces are left.")
        else:
            print(f"No more cake left! You need {abs(area-total)} pieces more.")
        break
    part = int(part)
    total += part

if area < total:
    print(f"No more cake left! You need {abs(area-total)} pieces more.")