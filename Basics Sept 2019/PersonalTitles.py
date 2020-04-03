age = float(input())
gen = str(input()).lower()

if age < 16:
    if gen == "m":
        print("Master")
    elif gen == "f":
        print("Miss")
if age >= 16:
    if gen == "m":
        print ("Mr.")
    elif gen == "f":
        print("Ms.")
