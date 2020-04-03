budget = float(input())
statisti = int(input())
obleklo = float(input())
dekor = budget - (budget * 0.9)

if statisti > 150:
    obleklo = obleklo - (obleklo * 0.1)

pari = obleklo * statisti
total = budget - (dekor + pari)

if total < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(total):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(total):.2f} leva left.")