# Usa una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el código fuente al contenedor
COPY GameSimulation.py /app/GameSimulation.py

# Comando que se ejecutará al iniciar el contenedor
CMD ["python", "GameSimulation.py"]
