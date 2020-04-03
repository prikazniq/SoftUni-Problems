type = input().lower()
rows = int(input())
columns = int(input())
income = 0
cinema_capacity = rows * columns

if type == "premiere":
    income = cinema_capacity * 12
elif type == "normal":
    income = cinema_capacity * 7.5
elif type == "discount":
    income = cinema_capacity * 5

print(f"{income:.2f}")