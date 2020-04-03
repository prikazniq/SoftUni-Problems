import math

loze = int(input())
grozdekvm = float(input())
needed = int(input())
rabotnici = int(input())
zadeleno = loze - (loze * 0.60)
kg_grozde = zadeleno * grozdekvm
litri = kg_grozde / 2.5

if litri < needed:
    print("It will be a tough winter! More {0} liters wine needed.".format(math.floor(needed - litri)))
elif litri > needed:
    print("Good harvest this year! Total wine: {0} liters.".format(math.floor(litri)))
    print("{0} liters left -> {1} liters per person.".format(math.ceil(litri-needed), math.ceil((litri-needed)/rabotnici)))
