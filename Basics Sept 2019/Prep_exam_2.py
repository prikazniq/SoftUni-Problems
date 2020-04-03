import math

w = float(input())
l = float(input())
h = float(input())
average_h = float(input())

volume = w * l * h
volume_room = (average_h + 0.4) * 2 * 2
space_left = math.floor(volume / volume_room)

if 3 < space_left <= 10:
    print(f"The spacecraft holds {space_left} astronauts.")
elif space_left > 10:
    print(f"The spacecraft is too big.")
elif space_left < 3:
    print(f"The spacecraft is too small.")
