class EngrRooms():
    def __init__(self,classes,description,next_class):
        self.classes = classes
        self.description = description
        self.next_class

    def get_classes(self):
        return self.classes

    def get_description(self):
        return self.description

    def list_classes(self):
        classes_str = ""
        for i in self.classes:
            classes_str += (f'{i}\n')
        return classes_str

    # gets a random class from incorrect classes, need two    
    def get_random_incorrect():
        return random.choice(list(incorrect_classes.values()))

    #def get_next_class(self):
        # if correct class is chosen, move onto the next class. 
        # if incorrect class is chosen, strike counter is set to 1/3 until 3/3.

    #def __str__(self):
     # return f'{self.name}: {self.description}\n\nClasses:\n{self.list_classes()}'
