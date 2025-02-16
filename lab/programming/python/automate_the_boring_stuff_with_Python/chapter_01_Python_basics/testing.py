#!/usr/bin/python3

message = "Hello world!"
name_message = "What is your first name?"
surname_message = "What is yolur surname?"
age = "How old are you?"

print(message)
print(name_message)
myName = input()
print (surname_message)
mySurname = input()
print(age)
myAge = int(input())

fullName = f"{myName.title()} {mySurname.title()}"

print("Here the information about you:")
print(f"Your full name is: {fullName}")
print(f"and you are {myAge} years old.")
print("Have fun learning python!")