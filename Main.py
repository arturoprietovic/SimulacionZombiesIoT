from Models.Building import Building
from Sim.Simulation import Simulation
from ConsoleView.MenuView import MenuView

def main():
    building = None
    simulation = Simulation()
    menu_view = MenuView()

    while simulation.isEveryoneInfected == False:
        
        menu_view.displayMainMenu()
        choice = menu_view.selectOption()

        if choice == "1":
            try:
                rooms = menu_view.enterRoomsPerFloor()
                floors = menu_view.enterFloorsCount()

                if rooms <= 0 or floors <= 0:
                    menu_view.displayInvalidInput()
                    continue

                building = Building(rooms_per_floor=rooms, floors_count=floors)
                simulation.configure(building)
                menu_view.displayBuildingConfigured()

            except ValueError:
                menu_view.displayInvalidInput()

        elif choice == "2":
            if simulation.building is None:
                menu_view.displayConfigureFirstError()
                continue
            
            menu_view.advanceSimulation()
            simulation.run()

        elif choice == "3":
            if simulation.building is None:
                menu_view.displayConfigureFirstError()
                continue

            simulation.view.displayBuildingStatus(building, simulation.infected_rooms)

        elif choice == "4":
            menu_view.displayExit()
            break

        else:
            menu_view.invalidChoice()

if __name__ == "__main__":
    main()
