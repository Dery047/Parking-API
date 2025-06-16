
````markdown
# Parking Management API (Django REST Framework)

A simple backend API for managing vehicle entries and exits in a parking lot, built using Django and Django REST Framework. The API automatically calculates the amount to pay based on the time a vehicle remains in the parking lot. (The base price per hour is set at $2 USD)

---

## Features

- Register vehicle entry and exit times  
- Automatic fee calculation based on time spent (default: $2/hour)  
- Validations to prevent invalid data (e.g., exit before entry)  
- Browsable DRF interface for quick testing  
- Admin panel for data management (optional)  

---

## Endpoints

| Method | Route                        | Description                        |
|--------|------------------------------|----------------------------------|
| GET    | `/api/vehicle-records/`      | Retrieve all vehicle records      |
| POST   | `/api/vehicle-records/`      | Create a new vehicle record       |
| GET    | `/api/vehicle-records/{id}/` | Retrieve a specific vehicle record by ID |
| PUT    | `/api/vehicle-records/{id}/` | Fully update a specific vehicle record  |
| PATCH  | `/api/vehicle-records/{id}/` | Partially update a specific vehicle record |
| DELETE | `/api/vehicle-records/{id}/` | Delete a specific vehicle record  |

---

## Tech Stack

- Python 3.12.13  
- Django 5.2.1  
- Django REST Framework  
- SQLite3  

---

## Installation & Setup

This project is part of my backend portfolio. Feel free to clone and run it locally! Here are the instructions to run it on your machine:

```bash
# Clone the repository
git clone https://github.com/your-username/parking-api.git
cd parking-api

# Create a virtual environment (optional but recommended)
python -m venv env
# Activate it:
source env/bin/activate   # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Run the development server
python manage.py runserver
````

---

# API de Gestión de Estacionamiento (Django REST Framework)

Una API backend simple para gestionar entradas y salidas de vehículos en un estacionamiento, construida con Django y Django REST Framework. La API calcula automáticamente el monto a pagar según el tiempo que un vehículo permanece en el estacionamiento. (El precio base por hora es \$2 USD)

---

## Funcionalidades

* Registrar horarios de entrada y salida de vehículos
* Cálculo automático de la tarifa basado en el tiempo (por defecto: \$2/hora)
* Validaciones para evitar datos inválidos (ej. salida antes de entrada)
* Interfaz navegable DRF para pruebas rápidas
* Panel de administración para gestión de datos (opcional)

---

## Endpoints

| Método | Ruta                         | Descripción                                     |
| ------ | ---------------------------- | ----------------------------------------------- |
| GET    | `/api/vehicle-records/`      | Obtener todos los registros de vehículos        |
| POST   | `/api/vehicle-records/`      | Crear un nuevo registro de vehículo             |
| GET    | `/api/vehicle-records/{id}/` | Obtener un registro específico por ID           |
| PUT    | `/api/vehicle-records/{id}/` | Actualizar completamente un registro específico |
| PATCH  | `/api/vehicle-records/{id}/` | Actualización parcial de un registro específico |
| DELETE | `/api/vehicle-records/{id}/` | Eliminar un registro específico                 |

---

## Tecnologías Usadas

* Python 3.12.13
* Django 5.2.1
* Django REST Framework
* SQLite3

---

## Instalación y Configuración

Este proyecto es parte de mi portafolio backend. Siéntete libre de clonarlo y ejecutarlo localmente! Aquí tienes las instrucciones para correrlo localmente

```bash
# Clona el repositorio
git clone https://github.com/tu-usuario/parking-api.git
cd parking-api

# Crea un entorno virtual (opcional pero recomendado)
python -m venv env
# Actívalo:
source env/bin/activate   # En Windows: env\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

# Aplica las migraciones
python manage.py migrate

# Crea un superusuario para acceso al admin
python manage.py createsuperuser

# Ejecuta el servidor de desarrollo
python manage.py runserver
```

```



