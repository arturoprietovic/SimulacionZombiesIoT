class Sensor:
    def __init__(self):
        self.state = "normal"
    
    def setAlert(self):
        self.state = "alert"

    def setNormal(self):
        self.state = "normal"

    def __str__(self):
        return f"Sensor with state {self.state}"

    