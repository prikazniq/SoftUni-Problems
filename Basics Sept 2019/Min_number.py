import sys

times = int(input())
count = 0
biggest = sys.maxsize

while count < times:
    count += 1
    current_number = int(input())
    if current_number < biggest:
        biggest = current_number

print(biggest)