class MenuView:
    @staticmethod
    def displayMainMenu():
        print("\n 🧟  Menú de Simulación 🏢")
        print("1️⃣  Configurar Edificio (Cantidad de Pisos y Habitaciones)")
        print("2️⃣  Avanzar Simulación por 1 Turno")
        print("3️⃣  Mostrar Estado Actual del Edificio")
        print("4️⃣  Salir")

    @staticmethod
    def selectOption():
        return input("Seleccione una opción (1-4): ")
    
    @staticmethod
    def enterRoomsPerFloor():
        return int(input("Ingrese la cantidad de habitaciones por piso: "))
    
    @staticmethod
    def enterFloorsCount():
        return int(input("Ingrese la cantidad de pisos: "))

    @staticmethod
    def displayInvalidInput():
        print("❌ Entrada inválida! Por favor, ingrese un valor numérico mayor a 0.")

    @staticmethod
    def displayBuildingConfigured():
        print("✅ Edificio configurado correctamente!")

    @staticmethod
    def displayConfigureFirstError():
        print("\n❌ Por favor, configure el edificio primero (Opción 1).")

    @staticmethod
    def advanceSimulation():
        print("\n🕒 Avanzando la Simulación ...")

    @staticmethod
    def displayExit():
        print("👋 Saliendo de la Simulación. ¡Adiós!")

    @staticmethod
    def invalidChoice():
        print("❌ Opción inválida! Por favor, seleccione una opción entre 1 y 4.")