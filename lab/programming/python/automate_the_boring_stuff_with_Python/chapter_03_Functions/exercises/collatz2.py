#!/usr/bin/python3

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def main():
    try:
        num = int(input("Enter an integer: "))
        if num <= 0:
            print("Please enter a positive integer.")
            return
        
        while num != 1:
            print(num, end=" → ")
            num = collatz(num)  # Update num with the new value
        
        print(1)  # Print the final 1

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
