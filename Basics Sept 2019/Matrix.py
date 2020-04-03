a = int(input())
b = int(input())
c = int(input())
d = int(input())

for top_left in range(a, b + 1):
    for top_right in range(a, b + 1):
        for bot_left in range(c, d + 1):
            for bot_right in range(c, d + 1):
                main_diagonal = top_left + bot_right
                second_diagonal = top_right + bot_left

                are_the_diag = main_diagonal == second_diagonal

                are_top_num = top_right != top_left
                are_bot_num = bot_left != bot_right

                if are_the_diag and are_bot_num and are_top_num:
                    print(f"{top_left}{top_right}\n{bot_left}{bot_right}")
                    print()