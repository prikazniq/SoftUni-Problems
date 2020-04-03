import math

type_of_year = input().lower()
praznici = int(input())
home = int(input())
sofia_weekends = 48 + praznici - home
sofia_play = (praznici - (praznici * 0.66)) - (48 - (48 * 0.2500))
total_play = sofia_weekends - sofia_play + home
if type_of_year == "normal":
    print(total_play)
elif type_of_year == "leap":
    leapyear = total_play + (total_play * 0.15)
    print(math.floor(leapyear))