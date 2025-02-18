try:
    # Get three numbers from the user
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))

    # Determine the largest number
    if first_number == second_number == third_number:
        print("All numbers are equal.")
    else:
        largest = max(first_number, second_number, third_number)
        print(f"The largest number is: {largest}")
except ValueError:
    print("Invalid input! Please enter integers only.")