grade = float(input())
if grade >= 5.50:
    print("Excellent")

first = int(input())
second = int(input())
if first > second:
    print(first)
else:
    print(second)

first = int(input())
if first % 2 == 0:
    print("even")
else:
    print("odd")

num = int(input())
if num == 1:
    print("one")
elif num == 2:
    print("two")
elif num == 3:
    print("three")
elif num == 4:
    print("four")
elif num == 5:
    print("five")
elif num ==6:
    print("six")
elif num == 7:
    print("seven")
elif num == 8:
    print("eight")
elif num == 9:
    print("nine")
else:
    print("number too big")

num = int(input())
if num < 100:
    print("Less than 100")
elif 100 <= num <= 200:
    print("Between 100 and 200")
elif num > 200:
    print("Greater than 200")

password = input()
if password == "s3cr3t!P@ssw0rd":
    print("Welcome")
elif password != "s3cr3t!P@ssw0rd":
    print("Wrong password!")

num = int(input())

if num == 1:
    print("Monday")
elif num == 2:
    print('Tuesday')
elif num == 3:
    print('Wednesday')
elif num == 4:
    print('Thursday')
elif num == 5:
    print('Friday')
elif num == 6:
    print('Saturday')
elif num == 7:
    print('Sunday')
else:
    print('Error')

animal = input().lower()
if animal == "dog":
    print("mammal")
elif animal in ("crocodile", "tortoise", "snake"):
    print("reptile")
else:
    print("unknown")
