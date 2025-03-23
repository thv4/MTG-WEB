#  MTG-WEB

¡Bienvenido a mi aplicación Django! Este es un proyecto que gestiona mazos de cartas de Magic: The Gathering.

---

## Requisitos previos

- Python 3.8 o superior.
- pip (gestor de paquetes de Python).
- Git (opcional, pero recomendado para clonar el repositorio).

---

## Instalación

1. **Clona el repositorio**:
  ```
  git clone https://github.com/thv4/MTG-WEB.git
  cd MTG-WEB
  ```
2. **Crea un entorno virtual** (recomendado):
  ```
  python -m venv .venv
  ```
3. **Activa el entorno virtual**:

    - En Linux/MacOS:
      ```
      source .venv/bin/activate
      ```
    - En Windows:
      ```
      .venv\Scripts\activate
      ```
4. **Instala las dependencias**:
  ```
  pip install -r requirements.txt
  ```
5. **Aplica las migraciones**:
  ```
  python manage.py migrate
  ```
6. **Crea un superusuario** (opcional, para acceder al panel de administración):
  ```
  python manage.py createsuperuser
  ```
7. **Ejecuta el servidor de desarrollo**:
  ```
  python manage.py runserver
  ```
