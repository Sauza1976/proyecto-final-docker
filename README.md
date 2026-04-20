## Descripción del Proyecto
Este proyecto es un **chatbot sencillo** desarrollado con **Flask** (Python) que responde a peticiones HTTP POST consultando un archivo JSON de respuestas predefinidas.
La aplicación está completamente **dockerizada**, permitiendo su despliegue en cualquier entorno sin preocuparse por dependencias ni configuraciones locales.

### ¿Qué hace?
- Recibe preguntas mediante peticiones HTTP POST al endpoint `/chat`
- Busca la respuesta correspondiente en un archivo `data.json`
- Devuelve la respuesta en formato JSON
- Si la pregunta no existe, responde: *"No entiendo la pregunta"*

- ### ¿Cómo funciona?
- Tú envías una pregunta desde tu ordenador
- La aplicación Flask (en app/main.py) está escuchando en el puerto 5000. Cuando llega una petición
- El programa abre el archivo data.json y busca si existe tu pregunta
- Si encuentra "hola" , Devuelve "Hola, ¿qué tal?"
  Si NO encuentra la pregunta → Devuelve "No entiendo la pregunta"
- Devuelve la respuesta en formato JSON

  ## Instrucciones de Instalación y Despliegue
### 1. Clonar el repositorio
git clone https://github.com/Sauza1976/proyecto-final-docker.git
cd proyecto-final-docker
### 2.  Construir la imagen con Docker
docker build -t chatbot-flask .
### 3. Levantar los servicios con Docker Compose
docker compose up --build
### 4. Acceder a la aplicación
- **URL local:** `http://localhost:5000`
- **Endpoint del chatbot:** `http://localhost:5000/chat`
- **Método:** `POST`
- **Content-Type:** `application/json`

  ##  Explicación de los Archivos Docker

### Dockerfile

**FROM** python:3.11-slim          # Imagen base ligera de Python 3.11

**WORKDIR** /app                    # Directorio de trabajo dentro del contenedor

**COPY** requirements.txt .        # Copiar archivo de dependencias

**RUN** pip install -r requirements.txt     # Instalar Flask

**COPY** . .                   # Copiar todo el código fuente al contenedor

**EXPOSE** 5000                # Puerto que expone la aplicación

**CMD** ["python", "app/main.py"]  # Comando de inicio

### docker-compose.yml
**version:** '3.8'                      # Versión del formato de Docker Compose

**services:**                           # Definición de los servicios

**chatbot:**                          # Nombre del servicio

**build:** .                        # Construye la imagen desde el Dockerfile local

**ports:**
      - "5000:5000"                    # Mapeo: puerto del host : puerto del contenedor
      
**volumes:**
      - ./app/data.json:/app/app/data.json   # Volumen para datos persistentes

## Posibles Problemas y Soluciones
      

| Problema                                            | Causa                                                                     | Solución                                                                     |
| --------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Error: Puerto 5000 en uso**                       | Otro servicio o contenedor ocupa el puerto                                | Cambiar el mapeo en docker-compose.yml: ports: - "5001:5000"                 |
| **Permiso denegado al ejecutar Docker**             | El usuario no pertenece al grupo docker                                   | Ejecutar: sudo usermod -aG docker \$USER y cerrar y volver a abrir la sesión |
| **Cambios en data.json no se reflejan**             | El volumen no está montado correctamente o hay caché                      | Reconstruir el contenedor: docker compose up --build                         |
| **La imagen no se construye**                       | Error de sintaxis en el Dockerfile o falta requirements.txt               | Revisar que los archivos existen y la sintaxis es correcta                   |
| **El contenedor se detiene inmediatamente**         | Error en la aplicación Flask (ruta mal, archivo JSON no encontrado, etc.) | Ver los logs: docker compose logs chatbot                                    |
| **No se puede acceder desde otro equipo de la red** | Flask solo escucha en localhost (127.0.0.1)                               | Asegurarse de que en main.py está: app.run(host="0.0.0.0", port=5000)        |

##  Contribuciones y Organización del Proyecto

Este proyecto utiliza un modelo de ramas en GitHub para mantener el código organizado y permitir el desarrollo paralelo sin afectar la versión estable.

### Estructura de ramas

| Rama | Propósito |
|------|-----------|
| **master** | Contiene el código estable y funcional listo para producción |
| **develop** | Rama de desarrollo donde se integran las nuevas funcionalidades antes de pasar a master |
| **feature/chatbot** | Rama específica para trabajar en la funcionalidad del chatbot de forma independiente |

### Flujo de trabajo paso a paso

**1. Inicializar el repositorio local**

Se inicializa Git en la carpeta del proyecto y se configura el usuario para identificar los commits.

**2. Primer commit en master**

Se añaden todos los archivos y se guarda el estado inicial del proyecto ya dockerizado.

**3. Crear ramas de desarrollo**

Se crea la rama develop para integración continua y la rama feature/chatbot para trabajar en nuevas funcionalidades.

**4. Commits en la rama de funcionalidad**

Se guardan los cambios realizados en el chatbot dentro de la rama correspondiente.

**5. Conectar con GitHub**

Se establece el enlace entre el repositorio local y el remoto creado en GitHub.

**6. Subir las ramas al repositorio remoto**

Se suben todas las ramas para tener copias en la nube y facilitar el trabajo colaborativo.

**7. Crear Pull Request y fusionar**

Desde GitHub se crea un Pull Request comparando feature/chatbot con master. Se revisan los cambios y se fusionan sin conflictos mediante el botón Merge pull request.

---

### Resultado final en GitHub

- El repositorio proyecto-final-docker contiene 3 ramas
- La rama master integra los cambios aprobados desde feature/chatbot
- El historial de commits queda documentado con los mensajes descriptivos


      
  ### Arquitectura del proyecto:

Usuario
↓

Interfaz Tkinter
↓

Lógica del chatbot en Python
↓

Archivo base_datos.json (preguntas y respuestas)
↓

Contenedor Docker
↓

Orquestación con Docker Compose
