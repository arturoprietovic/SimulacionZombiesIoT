from Models.Floor import Floor

class Building:
    def __init__(self, rooms_per_floor, floors_count):
        self.rooms_per_floor = rooms_per_floor
        self.floors_count = floors_count
        self.floors = []
        self.setUpFloors()

    def setUpFloors(self):
        for i in range(self.floors_count):
            self.floors.append(Floor(i, self.rooms_per_floor))

    def __str__(self):
        return f"Building with {self.floors_count} floors"