'''
Author:         GRETCHEN GOETHALS
Date:           4/25/2024
Assignment:     Project 2
Course:         CPSC1051
Lab Section:    SECTION 001

CODE DESCRIPTION: Create a text-based RPG game that uses classes and objects to facilitate the game. 

'''

# Import all modules and classes and random

# from GameMap import GameMap

from EngrRooms import EngrRooms
from BonusItems import BonusItems
from RaiseError import RaiseError
from Player import Player
import random


# Basic main print_classes function so that the classes print out with numbers next to them.

def print_classes(engr_rooms, display_list, incorrect_list):
     
    count = 1
    for choice in display_list:
        if(choice in incorrect_list):
            print(f"{count}) {choice}: {engr_rooms.get_description_incorrect(choice)}") # comment this out when code works
        else:
            print(f"{count}) {choice}: {engr_rooms.get_description(choice)}")
        count += 1
    print()

# Main function

def main():
  
# List of possible randomized incorrect classes

    incorrect_classes = {
        'IE 2100': 'Intro to Industrial Engineering',
        'ENGR 2100': 'Autocad',
        'MSE 2010': 'Intro to Materials Science',
        'IE 3010': 'Systems Design',
        'CPSC 1010': 'Intro to C',
        'MATH 3110': 'Linear Algebra',
        'IE 4400': 'Decision Support Systems',
        'IE 3860': 'Production Planning Control',
        'ART 2100': 'Art Appreciation',
        'SOC 2010': 'Intro to Sociology'
        }

# List of possible correct classes

    correct_classes = {
        'IE 3800': 'Operational Research',
        'IE 3840': 'Engineering Economic Analysis',
        'CPSC 1050': 'Programming in Python',
        'IE 3600': 'Probability and Statistics',
        'ENGL 2130': 'British Literature'
    }

# Initializing variables for classes to call later

    player = Player()
    engr_rooms = EngrRooms(correct_classes,incorrect_classes)
    raise_error = RaiseError()

# Initializing strike counter and correct counter

    strikes = 0
    correct_count = 0
    
# First print statements yay!

    print("You are an Industrial Engineering Student at Clemson University and it's the first day of classes!\n")
    print('Are you excited?! Y/N')

# Initializing a variable for the function in raise error class
        
    excited = raise_error.excited_error()

# If excited questions to ask user and print statements that follow

    if excited == 'y':
        print("Awesome. Let's get started. There's one thing to note before you start. If you don't make it on time to all of your classes on the first day, YOU (might) FAIL.\n")
    elif excited == 'n':
        print("Well you should be because you chose this major! No going back now! Anyways, let's get started. There's one thing to note before you start. If you don't make it on time to all of your classes on the first day, YOU (might) FAIL.\n")


    print("Here's your choice of classes and one is the correct choice. Be careful! Remember you have 3 strikes before you FAIL.\n")

# Initiate a while loop as long as the player's selected code is before 5 and the stikes are under 3. 

    while player.selected_correct_count < 5 and strikes < 3:
        display_incorrect = engr_rooms.get_random_incorrect()   # Random incorrect class is returned

        display_incorrect2 = engr_rooms.get_random_incorrect()  # Another random incorrect class is returned

# While loop within another while loop to prevent the repetition of incorrect classes

        while display_incorrect == display_incorrect2:  
            display_incorrect2 = engr_rooms.get_random_incorrect()

        correct_list = list(correct_classes.keys())             # Correct list created containing the keys of correct classes dictionary

        incorrect_list = list(incorrect_classes.keys())         # Incorrect list created containing the keys of incorrect classes dictionary

        display_correct = correct_list[player.selected_correct_count]   # Variable created to display the correct class based on the correct selection by the player

        display_list = [display_incorrect, display_incorrect2, display_correct]     # List created to hold the two incorrect classes and the one correct class

        random.shuffle(display_list)    # Shuffles the variables in the list so that they aren't in order

        print_classes(engr_rooms, display_list, incorrect_list) # Calls the function print_classes to display the number of classes and the type of classes



# Ask user to input the number of class they want by creating variable choice

        choice = input("Enter the number of the correct class: ")

# while True loop so that the loop continues until the code breaks

        while True:
            if choice.isdigit() and 1 <= int(choice) <= 3:  # If the choice is a number, and its between 1 and 3

                if display_list[int(choice) - 1] == display_correct:    # Checking if the correct choice is in the first index (0) and so on
                        
                    player.get_next_class(selected_correct = True)      # Then the next class function operates because the selected correct class is True
                        
                    break
                else:
                    strikes += 1    # Strikes go up if the correct choice is not picked

                    if strikes == 3:    # When the strikes reach 3, then you fail and print statement prints

                        print("You've reached 3 strikes. YOU FAIL. Looks like you suit the business life if you can't even make it on time.")

                        return  # Can't break, so return

                    print(f'Incorrect class chose. Strike counter: {strikes}/3. Be careful!')   # Strikes will count out of three

                    print_classes(engr_rooms, display_list, incorrect_list) # Calls the function print_classes to display the number of classes and the type of classes

                    choice = input("Enter the number of the correct class: ") # Ask user to input the number of class they want by creating variable choice

                       

            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

                choice = input("Enter the number of the correct class: ") # Ask user to input the number of class they want by creating variable choice

    if player.selected_correct_count == 5:  # When the selected amount of classes reach five, then you win!

        print("Congratulations! You've attended all of your classes on time! You win life as an engineer! How exciting.")
        return

# End of main function

if __name__ == "__main__":
    main()