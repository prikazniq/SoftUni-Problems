import math

needed_hours = int(input())
days_ava = int(input())
workers = int(input())
tenpercent = (days_ava - (days_ava * 0.1))
days_to_hours = tenpercent * 10 * workers
if days_to_hours > needed_hours:
    print("Yes!{0} hours left.".format(math.trunc((days_to_hours - needed_hours))))
elif days_to_hours < needed_hours:
    print("Not enough time!{0} hours needed.".format(math.trunc(days_to_hours - needed_hours)*-1))