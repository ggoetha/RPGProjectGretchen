import random

class EngrRooms():
    def __init__(self,classes,incorrect_classes):
        self.classes = classes
        self.next_class = " "
        self.incorrect_classes = incorrect_classes

    def get_classes(self):
        return self.classes

    def get_description(self, key):
        return self.classes[key]
    
    def get_description_incorrect(self, key):
        return self.incorrect_classes[key]

    def list_classes(self):
        classes_str = ""
        for i in self.classes:
            classes_str += (f'{i}\n')
        return classes_str

    # gets a random class from incorrect classes, need two    
    def get_random_incorrect(self):
        return random.choice(list(self.incorrect_classes.keys()))

    #def get_next_class(self):
        # if correct class is chosen, move onto the next class. 
        # if incorrect class is chosen, strike counter is set to 1/3 until 3/3.

    #def __str__(self):
     # return f'{self.name}: {self.description}\n\nClasses:\n{self.list_classes()}'
