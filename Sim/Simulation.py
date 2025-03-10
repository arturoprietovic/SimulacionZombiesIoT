import random
from ConsoleView.SimView import SimView

class Simulation:
    def __init__(self):
        self.infected_rooms = set()
        self.view = SimView()
        self.simHasStarted = False
        self.isEveryoneInfected = False
        self.building = None

    def configure(self, building):
        self.building = building

    def run(self):
        if not self.simHasStarted:
            self.startOutbreak()
            self.simHasStarted = True
        else:
            self._spread_zombies()
        if self.everyoneInfected():
            self.view.displayEveryoneInfected()
        self.view.displayBuildingStatus(self.building, self.infected_rooms)

    def startOutbreak(self):
        floor_index = random.randint(0, self.building.floors_count - 1)
        room_index = random.randint(0, self.building.rooms_per_floor - 1)
        infected_room = self.building.floors[floor_index].rooms[room_index]
        infected_room.sensor.setAlert()
        self.infected_rooms.add((floor_index, room_index))
        self.view.displayOutBreakStart(floor_index, room_index)

    def everyoneInfected(self):
        self.isEveryoneInfected = len(self.infected_rooms) == self.building.floors_count * self.building.rooms_per_floor
        return self.isEveryoneInfected

    def _spread_zombies(self):
        new_infected_rooms = set()

        for floor_index, room_index in self.infected_rooms:
            self._try_infect(floor_index, room_index - 1, new_infected_rooms)
            self._try_infect(floor_index, room_index + 1, new_infected_rooms)

            self._try_infect(floor_index - 1, room_index, new_infected_rooms)
            self._try_infect(floor_index + 1, room_index, new_infected_rooms)

        self.infected_rooms.update(new_infected_rooms)

    def _try_infect(self, floor_index, room_index, new_infected_rooms):
        if self._room_within_bounds(floor_index, room_index):
            if (floor_index, room_index) not in self.infected_rooms:
                self.building.floors[floor_index].rooms[room_index].sensor.setAlert()
                new_infected_rooms.add((floor_index, room_index))

    def _room_within_bounds(self, floor_index, room_index):
        return 0 <= floor_index < self.building.floors_count and 0 <= room_index < self.building.rooms_per_floor

 