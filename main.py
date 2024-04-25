'''
Author:         GRETCHEN GOETHALS
Date:           4/25/2024
Assignment:     Project 2
Course:         CPSC1051
Lab Section:    SECTION 001

CODE DESCRIPTION: Create a text-based RPG game that uses objects to facilitate the game. 

'''

# Initialize main

from GameMap import *
from EngrRooms import *
from BonusItems import *
from RaiseError import *
import random

count = 0


def main():
  

   # game_map = GameMap()

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

    correct_classes = {
        'IE 3800': 'Operational Research',
        'IE 3840': 'Engineering Economic Analysis',
        'CPSC 1050': 'Programming in Python',
        'IE 3600': 'Probability and Statistics',
        'ENGL 2130': 'British Literature'
    }
    

    inventory = []
    count = 0

    print("You are an Industrial Engineering Student at Clemson University and it's the first day of classes!\n")
    print('Are you excited?! Y/N')

    while True:
        excited = input().lower().strip()
        

        if excited == 'y':
            print("Awesome. Let's get started. There's one thing to note before you start. If you don't make it on time to all of your classes on the first day, YOU (might) FAIL.")

        elif excited == 'n':
            print("Well you should be because you chose this major! No going back now! Anyways, let's get started. There's one thing to note before you start. If you don't make it on time to all of your classes on the first day, YOU (might) FAIL.")
        
        else:
            print('Please give a valid answer.')

        engr_rooms = EngrRooms(classes,description,next_class)

        display_incorrect = engr_rooms.get_random_incorrect()
        display_correct = random.choice(list(correct_classes.values()))
        display_list = [display_incorrect] * 2 + [display_correct]
        random.shuffle(display_list)
        print(display_list)

        print("Here's your choice of classes and one is the correct choice. Be careful! Remember you have 2 strikes before you FAIL.\n")

        # How do I do a random shuffle of the classes in display list, then print the list so that we have two incorrect ie classes and one correct ie class?
            


# End of main function

if __name__ == "__main__":
    main()