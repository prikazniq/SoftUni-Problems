import sys

times = int(input())
sum = 0
min_number = sys.maxsize
max_number = -sys.maxsize

for every_time in range(times):
    num_for = int(input())
    if num_for > max_number:
        max_number = num_for
    if min_number > num_for:
        min_number = num_for

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")