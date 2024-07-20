DevOps Assessment

Este es un microservicio desarrollado para la evaluación técnica de DevOps. Utiliza Flask, Docker y Nginx para crear un entorno balanceado de carga.

REQUISITOS

- Python 3.8 o superior
- Flask
- Docker
- Docker Compose

INSTRUCCIONES

1. Clonar el repositorio.
2. Crear y activar un entorno virtual.
3. Instalar las dependencias.
4. Ejecutar la aplicación.

CLONAR EL REPOSITORIO

git clone https://github.com/cyberjoda25/neoris.git
cd neoris

CREAR Y ACTIVAR UN ENTORNO VIRTUAL

En Windows:
    python -m venv venv
    venv\Scripts\activate

En macOS/Linux:
    python3 -m venv venv
    source venv/bin/activate

INSTALAR LAS DEPENDENCIAS

pip install -r requirements.txt

EJECUTAR LA APLICACIÓN

python python3 app/app.py

Para probar la aplicacion puedes utilizar CURL en otra terminal

curl -X POST \
-H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" \
-H "Content-Type: application/json" \
-d '{"message": "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec": 45}' \
http://127.0.0.1:5000/DevOps


DOCKER

1) Construir y Levantar los Servicios con Docker Compose
2) Asegúrate de que Docker y Docker Compose están instalados y corriendo en tu máquina.
3) docker-compose up --build
Esto construirá las imágenes de Docker y levantará los servicios definidos en tu archivo docker-compose.yml.
