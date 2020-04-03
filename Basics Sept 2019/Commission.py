city = input().lower()
sells = float(input())
total = 0

if city == "sofia":
    if 0 <= sells <= 500:
        total = (5 / 100) * sells
        print(f"{total:.2f}")
    elif 500 <= sells <= 1000:
        total = (7 / 100) * sells
        print(f"{total:.2f}")
    elif 1000 <= sells <= 10000:
        total = (8 / 100) * sells
        print(f"{total:.2f}")
    elif sells >= 10000:
        total = (12 / 100) * sells
        print(f"{total:.2f}")
if city == "varna":
    if 0 <= sells <= 500:
        total = (4.5 / 100) * sells
        print(f"{total:.2f}")
    elif 500 <= sells <= 1000:
        total = (7.5 / 100) * sells
        print(f"{total:.2f}")
    elif 1000 <= sells <= 10000:
        total = (10 / 100) * sells
        print(f"{total:.2f}")
    elif sells >= 10000:
        total = (13 / 100) * sells
        print(f"{total:.2f}")

if city == "plovdiv":
    if 0 <= sells <= 500:
        total = (5.5 / 100) * sells
        print(f"{total:.2f}")
    elif 500 <= sells <= 1000:
        total = (8 / 100) * sells
        print(f"{total:.2f}")
    elif 1000 <= sells <= 10000:
        total = (12 / 100) * sells
        print(f"{total:.2f}")
    elif sells >= 10000:
        total = (14.5 / 100) * sells
        print(f"{total:.2f}")

if total <= 0:
    print("error")