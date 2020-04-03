vnoski = int(input())
counter = 0
smetka = 0

while counter < vnoski:
    money = float(input())
    if money < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {money:.2f}")
    smetka += money
    counter += 1

print(f"Total: {smetka:.2f}")
