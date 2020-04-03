work_days =  int(input())
money_per_day = float(input())
kurs = float(input())
earned = ((work_days*money_per_day) * 12 + (work_days*money_per_day * 2.5))
after_dds = earned - (earned * 0.25)
after_kurs = after_dds * kurs
avg_per_day = after_kurs / 365
print(round(avg_per_day, 2))
