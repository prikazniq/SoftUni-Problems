coin = float(input())

counter_2_lev = 0
counter_1_lev = 0
counter_50_stot = 0
counter_20_stot = 0
counter_10_stot = 0
counter_5_stot = 0
counter_2_stot = 0
counter_1_stot = 0
coin_left = 0

while coin > 0:
    while coin >= 2:
        coin_left = round((coin - 2), 2)
        counter_2_lev += 1
        coin = coin_left
    while coin >= 1:
        coin_left = round((coin - 1), 2)
        counter_1_lev += 1
        coin = coin_left
    while coin >= 0.5:
        coin_left = round((coin - 0.5), 2)
        counter_50_stot += 1
        coin = coin_left
    while coin >= 0.2:
        coin_left = round((coin - 0.2), 2)
        counter_20_stot += 1
        coin = coin_left
    while coin >= 0.1:
        coin_left = round((coin - 0.1), 2)
        counter_10_stot += 1
        coin = coin_left
    while coin >= 0.05:
        coin_left = round((coin - 0.05), 2)
        counter_5_stot += 1
        coin = coin_left
    while coin >= 0.02:
        coin_left = round((coin - 0.02), 2)
        counter_2_stot += 1
        coin = coin_left
    while coin >= 0.01:
        coin_left = round((coin - 0.01), 2)
        counter_1_stot += 1
        coin = coin_left

total = counter_2_lev + counter_1_lev + counter_50_stot + counter_20_stot + counter_10_stot + counter_5_stot + counter_2_stot + counter_1_stot


if coin == 0:
    print(total)