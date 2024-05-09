# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia todo el contenido del directorio de la aplicación al directorio de trabajo en el contenedor
COPY src/ .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8000 en el contenedor
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]