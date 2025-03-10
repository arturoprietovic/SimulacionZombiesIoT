from Models.Room import Room

class Floor:
    def __init__(self, floor_count, rooms_count):
        self.floor_count = floor_count
        self.rooms_count = rooms_count
        self.rooms = []
        self.setUpRooms(rooms_count)

    def setUpRooms(self, roomsCount):
        for i in range(roomsCount):
            self.rooms.append(Room(i))
    