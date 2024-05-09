## Administración de contenedores y servicios:

# Listar todos los contenedores (incluyendo los detenidos):
    $ docker ps -a

# Iniciar contenedores definidos en docker-compose.yml (en el directorio del archivo):
    $ docker compose up -d

# Detener y eliminar contenedores y redes definidos en docker-compose.yml (en el directorio del archivo):
    $ docker compose down

# Ver los logs de un contenedor específico:
    $ docker compose logs [nombre_del_servicio]



## Administración de imágenes:

# Construir una imagen a partir de un Dockerfile (en el directorio que contiene el Dockerfile):
    $ docker build -t bluehorizon:v1.0 .

# Listar imágenes locales:
    $ docker images

# Eliminar una imagen local:
    $ docker rmi nombre_de_la_imagen:tag



## Administración de contenedores individuales:

# Iniciar un contenedor específico definido en docker-compose.yml:
    $ docker compose up -d app

# Iniciar un contenedor específico "base de datos":
    $ docker compose up -d mydb

# Detener un contenedor específico:
    $ docker stop nombre_del_contenedor

# Eliminar un contenedor específico (forzando la detención si está en ejecución):
    $ docker rm -fv nombre_del_contenedor
