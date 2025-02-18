try:
    firstNumber = int(input("Enter a fisrt number: "))
    secondNumber = int(input("Enter a second number: "))
    thirdNumber = int(input("Enter a third number: "))


    if secondNumber < firstNumber > thirdNumber:
        print(f"{firstNumber} is the largest number.")
    elif firstNumber < secondNumber > thirdNumber:
        print(f"{secondNumber} is the largest number.")
    else:
        print(f"{thirdNumber} is the largest number.")
except ValueError:
    print("Invalid input! Please enter integers only.")
