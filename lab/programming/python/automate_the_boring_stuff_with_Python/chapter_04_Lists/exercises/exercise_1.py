#!/usr/bin/python3

import random

numberOfStreaks = 0  # Count how many experiments have at least one streak

for experimentNumber in range(10000):  # Run 10,000 experiments
    # Generate a list of 100 random 'H' or 'T' values
    myList = [random.choice(['H', 'T']) for _ in range(100)]
    
    # Debugging: Uncomment to see one trial's coin flips
    # print(myList)  
    
    # Check for streak of 6
    streak = 1  # Start streak count
    for i in range(1, len(myList)):
        if myList[i] == myList[i - 1]:  # Compare with previous flip
            streak += 1
            if streak == 6:  # Found a streak of 6
                numberOfStreaks += 1
                
                # Debugging: Show the list where a streak was found
                #print(f"Streak found in experiment {experimentNumber}: {myList}") 
                
                break  # Stop checking once we confirm a streak
        else:
            streak = 1  # Reset streak counter if different flip

# Calculate and print probability
print(f"Chance of streak: {numberOfStreaks / 10000 * 100:.2f}%")
