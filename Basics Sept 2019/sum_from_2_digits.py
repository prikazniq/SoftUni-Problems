start = int(input())
end = int(input())
magic = int(input())
combination = 0

for x1 in range(start, end + 1):
    for x2 in range(start, end + 1):
        combination += 1
        if x1 + x2 == magic:
            print(f"Combination N:{combination} ({x1} + {x2} = {magic}) ")
            break
    if x1 + x2 == magic:
        break

if x1 + x2 != magic:
    print(f"{combination} combinations - neither equals {magic}")
