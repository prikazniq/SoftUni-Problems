hours = int(input())
min = int(input())
after15 = min + 15
if hours == 23 and min > 44:
    hours = -1
if after15 > 59:
    hours += 1
    after15 = after15 - 60
if after15 > 59:
    hours += 1
    after = after15 - 60
if after15 < 10:
    print(f'{hours}:0{after15}')
else:
    print(f'{hours}:{after15}')