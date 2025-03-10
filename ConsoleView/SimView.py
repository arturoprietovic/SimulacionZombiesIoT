class SimView:
    @staticmethod
    def displayOutBreakStart(floor, room):
        print(f"\n🚨 El sensor de alerta de Zombie se activó en el piso {floor + 1} y habitación {room + 1} 🚨\n")

    @staticmethod
    def displayInitialState():
        print("\n📍 Estado inicial del edificio:")


    @staticmethod
    def displayBuildingStatus(building, infected_rooms):
        print("\n🏢 Estado del edificio 🏢\n")
        
        for floor_index in reversed(range(building.floors_count)):
            floor = building.floors[floor_index]
            
            floor_status = "| "  # Add floor label
            for room_index, room in enumerate(floor.rooms):
                state = "🧟" if (floor_index, room_index) in infected_rooms else "⬜"
                floor_status += state + " "

            print(floor_status + "|")  

        print("   " + "-" * (building.rooms_per_floor * 3))  
        print("🧟  Habitaciones con alerta: " + str(len(infected_rooms)))
        print("⬜  Habitaciones normales: " + str(building.floors_count * building.rooms_per_floor - len(infected_rooms)))

    @staticmethod
    def displayEveryoneInfected():
        print("\n🧟 ¡Todos están infectados! 🧟")