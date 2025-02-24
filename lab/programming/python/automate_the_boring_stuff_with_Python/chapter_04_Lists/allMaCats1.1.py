#!/usr/bin/python3

cat_names = []

while True:
    print(f"Enter the name of cat {str(len(cat_names) + 1)} (Or enter nothing to stop.):")
    name = input()

    if name == '':
        break
    
    cat_names.append(name)

print('The cat names are: ')

[print(name) for name in cat_names]
