widght = int(input())
lenght = int(input())
height = int(input())

volume = widght * lenght * height

counter_boxes = input()
volume_counter = 0
is_free = True

while not counter_boxes == "Done":
    counter_boxes = int(counter_boxes)
    volume_counter += counter_boxes

    if volume_counter > volume:
        is_free = False
        break

    counter_boxes = input()

if is_free:
    print(f"{volume - volume_counter} Cubic meters left.")
else:
    print(f"No more free space! You need {(volume - volume_counter) * -1} Cubic meters more.")
