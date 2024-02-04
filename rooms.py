directions = ["North", "East", "South", "West", "North east", "North west", "South east", 'South west']

class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}

    def get_name(self):
        return self.name

    def set_description(self, desc):
        self.description = desc

    def get_description(self):
        return self.description

    def describe(self):
        print("\n")
        print(self.get_description())
        print("\n")
        self.get_links()

    def set_links(self, direction, location):
        self.linked_rooms[direction] = location

    def get_links(self):
        for i in self.linked_rooms:
            room = self.linked_rooms[i]
            print("The", room.get_name(), "is to the", i)
        print("\n\n")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        elif direction in directions:
            print("You cannot go that way.")
            return self
        else:
            print("Invalid input.\n")
            return self