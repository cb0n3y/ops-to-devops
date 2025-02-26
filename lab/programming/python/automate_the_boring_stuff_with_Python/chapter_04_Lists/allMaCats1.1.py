#!/usr/bin/python3

# This program collects and prints the names of cats.

cat_names = []

while True:
    print(f"Enter the name of cat {len(cat_names) + 1} (Or enter nothing to stop.):")
    name = input()

    if name == '':
        break
    
    cat_names.append(name)

print('The cat names are: ')

for name in cat_names:
    print(name)
