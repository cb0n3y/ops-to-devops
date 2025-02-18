#!/usr/bin/python3

try:
    for number in range(1, 50):
        if (number % 3 == 0) and (number % 5 == 0):
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fuzz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)  # Print the number if it's not divisible by 3 or 5
except KeyboardInterrupt:
    print("\nProcess interrupted by user.")