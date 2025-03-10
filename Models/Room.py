from Models.Sensor import Sensor

class Room:
    def __init__(self, number):
        self.room_number = number
        self.sensor = Sensor()

    def getSensorState(self):
        return self.sensor.state
    
    def __str__(self):
        return f"Room {self.room_number} with sensor {self.sensor}"

    