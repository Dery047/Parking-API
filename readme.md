# Parking Management API (Django REST Framework)

A simple backend API for managing vehicle entries and exits in a parking lot, built using Django and Django REST Framework. The API automatically calculates the amount to pay based on the time a vehicle remains in the parking lot. (The base price per hour is set in $2USD)

---

## Features

- Register vehicle entry and exit times
- Automatic fee calculation based on time spent (default: $2/hour)
- Validations to prevent invalid data (e.g., exit before entry)
- Browsable DRF interface for quick testing
- Admin panel for data management (optional)

---

## Tech Stack

- Python 3.12.13
- Django 5.2.1
- Django REST Framework
- SQLite3

---

## nstallation & Setup if you want to run the file in your own device
 

 >  This project is part of my backend portfolio. Feel free to clone and run it locally! Here are the instructions to run it in your machine. 

```bash
# Clone the repository
git clone https://github.com/your-username/parking-api.git
cd parking-api

# Create a virtual environment (optional but recommended)
python -m venv env #activate it 
source env/bin/activate   # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Run the development server
python manage.py runserver

