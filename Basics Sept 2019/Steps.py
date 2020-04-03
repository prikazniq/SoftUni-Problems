steps_counter = 0
goal = 10000
is_reached = False

while steps_counter < goal:
    additional_steps = input()
    if additional_steps == "Going home":
        additional_steps = input()
        additional_steps = int(additional_steps)
        steps_counter += additional_steps
        if steps_counter >= goal:
            print("Goal reached! Good job!")
            is_reached = True
        else:
            print(f"{goal - steps_counter} more steps to reach goal.")
            is_reached = True
        break
    additional_steps = int(additional_steps)
    steps_counter += additional_steps


if not is_reached:
    print("Goal reached! Good job!")
