# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
#task1
apple_count = shelf.count('apples')
print("Number of Apples:",apple_count)
# task2
banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)
#task3
if apple_count <5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
# task4
grape_count = shelf.count("grapes")
if grape_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")
#task5
if "oranges" in shelf:
    print("Oranges are at index:", shelf.index('oranges'))
else:
    print("Oranges are out of stock.")

