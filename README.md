# Django REST Framework Project Setup

This project is built using Django REST Framework (DRF) and is managed with `pipenv` for dependency management. Follow the steps below to set up and run the project on your local machine.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or higher
- `pip` (Python package manager)
- `pipenv` (Install via `pip install pipenv` if not already installed)

## Setup Instructions
1. **Clone the repository**
```bash
git clone git@github.com:siperpus-udb/siperpus-api.git
cd siperpus-api
```
2. **Install Pipenv if you don't have**
```bash
pip install pipenv
```
3. **Activate the virtual environment**
```bash
pipenv shell
```
4. **Install the required dependencies**
```bash
pipenv install 
```
5. **Migrate the database**
```bash
python manage.py migrate
```
6. **Run the project**
```bash
python manage.py runserver 
```

Now you can access the server at https://localhost:8000
