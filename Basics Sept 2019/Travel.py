for dest in range(100):
    destination = input()
    if destination == "End":
        break
    needed_money = int(input())
    for money in range(100):
        installments = int(input())
        needed_money -= installments
        if needed_money <= 0:
            print(f"Going to {destination}!")
            break
        if installments == "End":
            break

destintaion2 = input()
while destintaion2 != "End":
    money_needed = float(input())
    savings = 0
    while savings < money_needed:
        current_sum = float(input())
        savings += current_sum
    print(f"Going to {destintaion2}!")
    destintaion2 = input()
