hour_exam = int(input())
min_exam = int(input())
hour_arrival = int(input())
min_arrival = int(input())
diff_min = 0
diff_hour = 0
after60 = 0

if hour_exam == hour_arrival and min_exam == min_arrival:
    print("On time")

if hour_exam == hour_arrival and min_exam < min_arrival:
    diff_min = min_arrival - min_exam
    print("Late")
    print(f"{diff_min} minutes after the start")

if hour_exam < hour_arrival:
    if min_exam < min_arrival or min_exam > min_arrival:
        diff_hour = hour_arrival - hour_exam
        diff_min = min_arrival + min_exam
        print("Late")
    if diff_min > 59:
        after60 = diff_min - 60
        print(f"{diff_hour + 1}:0{diff_min} hours after the start")
    if 0 < diff_min < 59:
        print(f"{diff_hour}:{diff_min} hours after the start")
    if diff_min == 59:
        if diff_hour >= 1:
            print(f"{diff_min} minutes after the start")

if hour_exam >= hour_arrival and min_exam >= min_arrival or min_exam < min_arrival:
    diff_hour = hour_exam - hour_arrival
    diff_min = min_exam - min_arrival
    print("Early")
    if diff_min > 59:
        after60 = diff_min - 60
        print(f"{diff_hour + 1}:0{diff_min} hours before the start")
    if 0 < diff_min < 59:
        print(f"{diff_hour}:{diff_min} hours before the start")
    if diff_min == 0:
        print(f"{diff_hour}:00 hours before the start")
    if diff_min < 0:
        after60 = 60 + diff_min
        print(f"{after60} minutes before the start")

if hour_exam >= hour_arrival and min_exam <= 0 or min_exam < 30 < min_arrival:
    diff_min = min_arrival - min_exam
    diff_hour = hour_arrival - hour_exam
    print("On time")
    if diff_hour == 0 or diff_hour <= 1:
        if diff_min > 59:
            after60 = diff_min - 60
            print(f"{diff_hour + 1}:0{diff_min} hours before the start")
        if 0 < diff_min <= 59:
            diff_min = 60 - min_arrival
            print(f"{diff_min} minutes before the start")
