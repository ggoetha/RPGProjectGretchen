from RaiseError import RaiseError   # Uses raise error in bonus classes, so import raise error from raise error

class BonusItems:

# Initializes hint message in a function

    def __init__(self):
        self.message = f" HINT: The next class you need to go to is one of the introduction classes you need for an Industrial Engineering Computing Emphasis. Goodluck!"

# Get message returns the message in the initializing function

    def get_message(self):
        return self.message

# Get item initializes a variable for raise error, prints a item statement and prompts the user to pick up the item

    def get_item(self):
        error = RaiseError()
        print("You found a piece of paper in this class. Pick it up? Y/N")
        choice = error.excited_error()
        while True:     # While loop if true, if the user wants to pick up the item then the hint is printed, if the user does not want to pick up the item then the game continues without printing the hint
            if choice == "y":
                print(self.get_message())
                return
            elif choice =="n":
                return
            else:
                choice = error.excited_error()
                continue

    