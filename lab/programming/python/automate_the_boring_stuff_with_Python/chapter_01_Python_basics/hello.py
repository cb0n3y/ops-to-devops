#!/usr/bin/python3

# This program says hello and ask for my name

print("Hello world!")

print("What's your name? ")
myName = input()
print(f"It is good to meet you {myName.title()}")
print(f"The length of your name is: {len(myName)}")

print("What's your age? ")
myAge = int(input())
print(f"You will be {myAge +1 } in a year.")