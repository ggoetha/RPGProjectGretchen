
from BonusItems import BonusItems

class Player(BonusItems):

    def __init__(self):
        self.strikes = 0
        self.selected_correct_count = 0
        self.bonus = BonusItems()

    def get_next_class(self,selected_correct):
        if selected_correct:
            self.selected_correct_count += 1
            print("You found your class! Great job! You attend your class on time. Moving onto the next class!\n")
            if self.selected_correct_count == 2:
                print(self.bonus.get_message())
                # call bonus item statement
                # return bonus item statement
                return

        else:
            self.strikes += 1
            print(f"Incorrect class chosen. Strike counter: {self.strikes}/3. Be careful!\n")
            if self.strikes == 3:
                print("You've reached 3 strikes. YOU FAIL. Looks like you suit the business life.")
                return