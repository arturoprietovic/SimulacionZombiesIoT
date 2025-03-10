# SimulacionZombiesIoT

## Ejecución

Se debe clonar el repositorio en local y ejecutar con Python usando ```python main.py```

## Arquitectura

Se usó la arquitectura propuesta, con las clases **Building**, **Floor**, **Room** y **Sensor**, que son modelos de datos y no contienen lógica; y **Simulation** que, dado el tamaño de la solución, contiene toda la lógica de la simulación. En caso de que se proponga escalar el programa a mayor complejidad, se debe separar la lógica en modulos. 

Además, se agregaron dos clases para manejar la interacción con el usuario: **SimView**, que se encarga de comunicar lo hecho por la simulación en cada turno. Y **MenuView**, que muestra lo relacionado al menú y pide inputs al usuario.

## Comandos

El menú tiene 4 comandos que se ejecutan mediante los números indicativos:

1️⃣  Configurar Edificio (Cantidad de Pisos y Habitaciones)
2️⃣  Avanzar Simulación por 1 Turno
3️⃣  Mostrar Estado Actual del Edificio
4️⃣  Salir

En el caso del 1️⃣, al elegirlo se piden los siguientes inputs:

Ingrese la cantidad de habitaciones por piso:
Ingrese la cantidad de pisos: