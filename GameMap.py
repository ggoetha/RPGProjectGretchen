class GameMap:
    def __init__(self):
        self.map = {}

    def select_room(self, room):
        self.map[room.get_name().lower()] = room

    def get_room(self,current):
        return self.map.get(current.lower())
        