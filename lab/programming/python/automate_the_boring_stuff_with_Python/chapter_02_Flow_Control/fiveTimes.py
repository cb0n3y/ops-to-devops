#!/usr/bin/python3

print('My name is')

for i in range(5):
    # use this if you want to start counting from 1 and not from 0.
    # i += 1
    print('Jimmy Five Times (' + str(i) + ')')


# The Starting, Stopping, and Stepping Arguments to range()
print()

for i in range(12, 16):
    print(i)

print()


# first two arguments are start and stop and the third one 
# will ber the step argument.
#
# Expected result: 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print(i)


# You can even use a negative number for step argument to make 
# the for loop count down instead of up.

print()

for i in range(5, -1, -1):
    print(i)