#!/usr/bin/python3

greetings = ['hello', 'hi', 'howdy', 'heyas']
animals = ['cat', 'hi', 'dog', 'hello', 'parrot', 'heyas', 'tiger', 'howdy']
greetings_found = []


for greeting in animals[:]:
    if greeting in greetings:
        greetings_found.append(greeting)
        animals.remove(greeting)


print("Here the content of the original greetings list:")
[print(greeting) for greeting in greetings]

print("Here the content of the found greetings list:")
[print(greeting) for greeting in greetings_found]