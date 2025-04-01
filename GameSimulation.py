import random

def selectExecution(randNumber, team):
    global ChivasPoints, AtlasPoints
    
    if 1 <= randNumber <= 100:
        print(f"{team} dispara desviado.")
    elif 101 <= randNumber <= 200:
        print(f"{team} dispara, pero el portero ataja la pelota.")
    elif 201 <= randNumber <= 250:
        print(f"{team} anota un gol de cabeza!")
        if team == "Chivas":
            ChivasPoints += 1
        else:
            AtlasPoints += 1
    elif 251 <= randNumber <= 300:
        print(f"{team} anota un gol de penal!")
        if team == "Chivas":
            ChivasPoints += 1
        else:
            AtlasPoints += 1
    elif 301 <= randNumber <= 350:
        print(f"{team} anota un gol con el pie!")
        if team == "Chivas":
            ChivasPoints += 1
        else:
            AtlasPoints += 1

# Inicializar variables de los equipos
ChivasPoints = 0
AtlasPoints = 0

# Simulación de los 90 minutos del partido
for minute in range(1, 91):
    print(f"Minuto {minute}:")
    # Seleccionar el equipo en turno
    turn = random.choice(["Chivas", "Atlas"])
    
    # Generar un número aleatorio dentro del rango de eventos
    randNumber = random.randint(1, 350)
    
    # Ejecutar la acción correspondiente
    selectExecution(randNumber, turn)
    print()

# Mostrar el resultado final
print("\nResultado Final:")
print(f"Chivas {ChivasPoints} - {AtlasPoints} Atlas")
