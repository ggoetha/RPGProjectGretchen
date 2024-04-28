import random   # Uses random function, so import random

# Class created for classes in engineering, initialized class, next class for a text string, and incorrect classes

class EngrRooms():
    def __init__(self,classes,incorrect_classes):
        self.classes = classes
        self.next_class = " "
        self.incorrect_classes = incorrect_classes

# Getting the class object, class description which is the key for the classes, and then the incorrect description which is the key for the classes

    def get_classes(self):
        return self.classes

    def get_description(self, key):
        return self.classes[key]
    
    def get_description_incorrect(self, key):
        return self.incorrect_classes[key]

# makes a list of the classes

    def list_classes(self):
        classes_str = ""
        for i in self.classes:
            classes_str += (f'{i}\n')
        return classes_str

# gets a random class from incorrect classes, need two   
 
    def get_random_incorrect(self):
        return random.choice(list(self.incorrect_classes.keys()))


