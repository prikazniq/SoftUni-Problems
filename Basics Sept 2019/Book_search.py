book_objective = input()
book_counter = int(input())
counter = 0
is_book_found = False

while book_counter > counter:
    current_book = input()
    if book_objective == current_book:
        is_book_found = True
        print(f"You checked {counter} books and found it.")
        break
    counter += 1
if not is_book_found:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")
