
from BonusItems import BonusItems

# Creates an inheritance class of Players from Bonus Items

class Player(BonusItems):

# Initializes a function with strikes, selected class count, and bonus items

    def __init__(self):
        self.strikes = 0
        self.selected_correct_count = 0
        self.bonus = BonusItems()

# A function for getting the next class if they select the correct class

    def get_next_class(self,selected_correct):
        if selected_correct:
            self.selected_correct_count += 1    # Counter adds one to correctly selected class

            print("You found your class! Great job! You attend your class on time. Moving onto the next class!\n")

            if self.selected_correct_count == 2:    # When the correct count gets to 2, then print the bonus item hint
                self.bonus.get_item()
                return

        # Add one to strikes if incorrect class is picked, until you get to three

        else:
            self.strikes += 1
            print(f"Incorrect class chosen. Strike counter: {self.strikes}/3. Be careful!\n")
            if self.strikes == 3:   # 3 Strikes, game breaks
                print("You've reached 3 strikes. YOU FAIL. Looks like you suit the business life.\n")
                return