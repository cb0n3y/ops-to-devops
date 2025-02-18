try:
    first_number = int(input("Eneter the first number: "))
    second_number = int(input("Enter the second number: "))

    number_sum = first_number + second_number

    print(f"{first_number} + {second_number} = {number_sum}")
except ValueError:
    print("Invalid input! PLease enter integer only")
