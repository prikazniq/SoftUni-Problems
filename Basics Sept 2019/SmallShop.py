product = str(input()).lower()
city = str(input()).lower()
quant = float(input())

if city == "sofia":
    if product == "coffee":
        print(0.50 * quant)
    if product == "water":
        print(0.80 * quant)
    if product == "beer":
        print(1.20 * quant)
    if product == 'sweets':
        print(1.45 * quant)
    if product == 'peanuts':
        print(1.6 * quant)
if city == "plovdiv":
    if product == "coffee":
        print(0.4 * quant)
    if product == "water":
        print(0.70 * quant)
    if product == "beer":
        print(1.15 * quant)
    if product == 'sweets':
        print(1.30 * quant)
    if product == 'peanuts':
        print(1.5 * quant)
if city == "varna":
    if product == "coffee":
        print(0.45 * quant)
    if product == "water":
        print(0.7 * quant)
    if product == "beer":
        print(1.10 * quant)
    if product == 'sweets':
        print(1.35 * quant)
    if product == 'peanuts':
        print(1.55 * quant)