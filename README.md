# Task Manager App

Este proyecto es una aplicación web desarrollada en Django que permite a los usuarios gestionar tareas. Los usuarios pueden crear, leer, actualizar y eliminar tareas (funcionalidad CRUD), así como registrarse, iniciar sesión y cerrar sesión. También incluye una API REST para interactuar con las tareas.

## Funcionalidades

- **Autenticación de usuarios**: Los usuarios pueden registrarse, iniciar sesión y cerrar sesión.
- **Gestión de tareas**: Los usuarios pueden crear, listar, editar y eliminar tareas.
- **API REST**: Permite interactuar con las tareas a través de endpoints API.
- **Interfaz con Bootstrap**: La aplicación tiene un diseño sencillo y atractivo gracias a la integración de Bootstrap.

## Requisitos

- Python 3.8 o superior
- Django 5.1
- Django REST Framework (para la API)
- Bootstrap 5 (para el diseño)

## Instalación

1. Clona este repositorio:
    ```bash
    git clone <URL_de_tu_repositorio>
    ```

2. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```

3. Activa el entorno virtual:
    - En Windows:
      ```bash
      venv\Scripts\activate
      ```
    - En Mac/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

5. Realiza las migraciones:
    ```bash
    python manage.py migrate
    ```

6. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

7. Abre el navegador y ve a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

## Estructura del Proyecto

- `tasks/`: Contiene la aplicación principal para gestionar tareas.
  - `views.py`: Define las vistas de la aplicación.
  - `models.py`: Define el modelo de datos `Task`.
  - `serializers.py`: Configura los serializadores para la API REST.
  - `urls.py`: Define las rutas URL de la aplicación.
  - `templates/`: Contiene las plantillas HTML de la aplicación.
  
## Rutas Disponibles

- **/register/**: Registro de usuario.
- **/login/**: Iniciar sesión.
- **/logout/**: Cerrar sesión.
- **/task-list/**: Lista de tareas del usuario autenticado.
- **/task/create/**: Crear una nueva tarea.
- **/task/<id>/edit/**: Editar una tarea.
- **/task/<id>/delete/**: Eliminar una tarea.
- **/task/<id>/detail/**: Ver detalles de una tarea.

## API REST (extra)

La aplicación también incluye una API REST para gestionar las tareas. Las rutas disponibles son:

- **GET /api/tasks/**: Obtener todas las tareas del usuario.
- **POST /api/tasks/**: Crear una nueva tarea.
- **GET /api/tasks/<id>/**: Obtener los detalles de una tarea.
- **PUT /api/tasks/<id>/**: Actualizar una tarea.
- **DELETE /api/tasks/<id>/**: Eliminar una tarea.
  
## Contribución

Si deseas contribuir a este proyecto, por favor realiza un fork y crea un pull request con tus mejoras.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).
