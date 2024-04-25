class BonusItems:
    def __init__(self,item):
        self.item = item
        self.message = f"The next class you need to go to is one of the introduction classes you need for an Industrial Engineering Computing Emphasis. Goodluck!"

    def get_message(self):
        return self.message




# item will contain a message and a hint for the next class when you pick it up