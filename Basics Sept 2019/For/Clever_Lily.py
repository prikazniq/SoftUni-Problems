age = int(input())
price_of_washing_machine = float(input())
money_for_toy = int(input())
toy_counter = 0
money_counter = 0

for toy in range(0, age + 1):
    if toy % 2 != 0:
        toy_counter += 1
    else:
        money_counter += 10 * (toy / 2)
        money_counter -= 1

money_counter += toy_counter * money_for_toy + 1

if money_counter >= price_of_washing_machine:
    print(f"Yes! {money_counter - price_of_washing_machine:.2f}")
else:
    print(f"No! {abs(money_counter - price_of_washing_machine):.2f}")

