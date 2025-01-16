## App para análisis de imágenes

Esta aplicación analiza imágenes y se puede ejecutar en el puerto 4500 desde el archivo `run.py`.

### Docker

Hay una imagen dockerizada disponible en DockerHub. Para utilizar la aplicación utilizando Docker, puedes hacer lo siguiente:
### Ejecución de la aplicación sin Docker

1. Abre una terminal en tu máquina local.
2. Navega al directorio donde se encuentra el archivo `run.py`.
3. Crea un ambiente virtual en Python con el siguiente comando:
    ```sh
    python -m venv venv
    ```
4. Activa el ambiente virtual:
    - En Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - En macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Instala los requerimientos necesarios utilizando el archivo `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```
6. Ejecuta la aplicación con el siguiente comando:
    ```sh
    python run.py
    ```
7. Abre tu navegador web y navega a `http://localhost:4500` para acceder a la aplicación.
### Pasos para descargar y ejecutar la imagen desde Docker Hub

1. Abre una terminal en tu máquina local.
2. Asegúrate de tener Docker instalado y funcionando correctamente.
3. Ejecuta el siguiente comando para descargar la imagen desde Docker Hub:
    ```sh
    docker pull rusticdevelop/image_analysis
    ```
4. Una vez descargada la imagen, ejecuta el siguiente comando para iniciar la aplicación:
    ```sh
    docker run -p 8000:4500 rusticdevelop/image_analysis
    ```
5. Abre tu navegador web y navega a `http://localhost:8000` para acceder a la aplicación.