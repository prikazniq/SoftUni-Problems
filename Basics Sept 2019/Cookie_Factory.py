batches_count = int(input())
for batch in range(1, batches_count+1):
    has_flour = False
    has_eggs = False
    has_sugar = False
    has_all_ingred = False
    product = ""
    while product != "Bake!":
        product = input()
        if product == "flour":
            has_flour = True
        elif product == "eggs":
            has_eggs = True
        elif product == "sugar":
            has_sugar = True
        has_all_ingred = has_sugar and has_eggs and has_flour
        if product == "Bake!":
            if has_all_ingred:
                print(f"Baking batch number {batch}...")
                break
            else:
                print(f"The batter should contain flour, eggs and sugar!")






