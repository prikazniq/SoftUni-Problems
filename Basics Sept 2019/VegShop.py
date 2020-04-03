veg_price = float(input())
fru_price = float(input())
veg_kg = float(input())
fru_kg = float(input())
vegie = veg_kg * veg_price
frutie = fru_kg * fru_price
price = vegie + frutie
euro = price / 1.94
print(euro)