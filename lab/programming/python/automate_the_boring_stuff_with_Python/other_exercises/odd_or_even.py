msg = "Enter a number"
number = int(input())

try:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")