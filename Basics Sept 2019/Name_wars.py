names = input()
final = 0
final_name = ""

while names != "STOP":
    current_sum = 0
    for char in names:
        current_sum += ord(char)
        if current_sum > final:
            final = current_sum
            final_name = names
    names = input()

print(f"Winner is {final_name} - {final}!")

