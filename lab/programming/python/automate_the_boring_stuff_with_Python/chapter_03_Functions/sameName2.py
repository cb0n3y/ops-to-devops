#!/usr/bin/python3


def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
