s = input()

if s == "banana" \
        or s == "kiwi"\
        or s == "apple"\
        or s == 'lemon'\
        or s == "grapes"\
        or s == "cherry":
    print("fruit")
elif s == "pepper"\
        or s == "cucumber"\
        or s == "carrot"\
        or s == "tomato":
    print("vegetable")
else:
    print("unknown")

num = float(input())
range = (100 <= num <= 200) or num == 0
if not range:
    print("invalid")

animal = input()
if animal == "dog":
    print("mammal")
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    print("reptile")
else:
    print("unknown")

type = input()
r = int(input())
c = int(input())
if type == "Premiere":
    prihod = r * c * 12
    print(prihod)
elif type == "Normal":
    prihod = r * c * 7.5
    print(prihod)
elif type == "Discount":
    prihod = r * c * 5
    print(prihod)


