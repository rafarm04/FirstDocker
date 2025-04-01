# Simulador de Fútbol Chivas vs. Atlas

Este proyecto simula un partido de fútbol entre las Chivas y el Atlas utilizando Python.  El simulador considera el turno de cada equipo y la duración de 90 minutos del partido, empleando números aleatorios para determinar los eventos del juego. 

## Funcionalidades:

El simulador genera eventos aleatorios durante los 90 minutos del partido, asignando turnos a cada equipo.   Los números aleatorios generados se interpretan de la siguiente manera:

* **1-100:** Disparo desviado del equipo en turno.
* **101-200:** Disparo atajado por el portero.
* **201-250:** Gol de cabeza.
* **251-300:** Gol de penal.
* **301-350:** Gol con el pie. 

El resultado final del partido se mostrará al finalizar los 90 minutos de simulación. 


## Ejecución:

El código fuente se encuentra en `GameSimulation.py`.   Para ejecutar la aplicación, se necesita un entorno Docker.  La configuración de Docker se encuentra en el archivo `Dockerfile`.   Una vez configurado el entorno, ejecutar el contenedor Docker para iniciar la simulación. 


## Tecnologías:

* Python 
* Docker 
