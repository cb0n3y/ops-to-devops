#!/usr/bin/python3

import random 


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
    elif number % 2 == 1:
        print(3 * number + 1)

collatz(random.randint(1,20))
