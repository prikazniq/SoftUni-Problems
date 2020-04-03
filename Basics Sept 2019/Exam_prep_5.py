begin = int(input())
stops = int(input())
total_odd = 0
total_even = 0
total1 = 0
total2 = 0

for i in range(1, stops + 1):
    getting_out = int(input())
    getting_in = int(input())
    if i % 2 == 0:
        total_even = getting_in - getting_out - 2
        total1 += total_even
    else:
        total_odd = getting_in - getting_out + 2
        total2 += total_odd

end = begin + (total2 + total1)

print(f"The final number of passengers is : {end}")