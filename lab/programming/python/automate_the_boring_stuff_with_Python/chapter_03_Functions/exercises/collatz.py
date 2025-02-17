#!/usr/bin/pyton3


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

collatz(6)
collatz(9)
collatz(123)
collatz(546)
