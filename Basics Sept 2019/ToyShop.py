vac = float(input())
puzzle = int(input())
talking_doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())
broiIgrachki = puzzle + talking_doll + bear + minion + truck
total = puzzle * 2.60 + talking_doll * 3 + bear * 4.10 + minion * 8.20 + truck * 2
after = 0

if broiIgrachki >= 50:
    total = total - (total * 0.25)

total = total - (total * 0.10)
tripmoney = total - vac

if tripmoney < 0:
    print(f"Not enough money! {abs(tripmoney):.2f} lv needed.")
else:
    print(f"Yes! {abs(tripmoney):.2f} lv left.")