#!/usr/bin/python3


# print('Enter the name of cat 1:')
# catName1 = input()
# print('Enter the name of cat 2:')
# catName2 = input()
# print('Enter the name of cat 3:')
# catName3 = input()
# print('Enter the name of cat 4:')
# catName4 = input()
# print('Enter the name of cat 5:')
# catName5 = input()

# Instead of using multipole, repetitive variables, you 
# can use a single variable that contains a list of values.

catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()

    if name == '':
        break
    
    catNames = catNames + [name] # list concatination

print('The cat names are: ')

for name in catNames:
    print(' ' + name)