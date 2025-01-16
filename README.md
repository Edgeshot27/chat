# ChatApp

ChatApp is a web-based messaging application built with Django and designed to be scalable and responsive. The application supports user authentication, dashboard functionality, and interactive features.

## Features
- User Authentication (Signup, Login, Logout).
- Dynamic page scaling based on screen resolution.
- Interactive sections like Dashboard, Messaging, and Settings.
- Styled with CSS for a modern, user-friendly interface.

---

## Requirements

To run this project, ensure the following are installed on your system:
- **Python 3.10** or above
- **Django**
- **Uvicorn** (for ASGI server support)
- **Redis** (if you're using Django Channels or plan to use asynchronous features)

---

## Installation Instructions

### Step 1: Clone the Repository
```bash
git clone <your-repository-url>
cd <project-directory>
```

### Step 2: Create a Virtual Environment
Create and activate a Python virtual environment to isolate project dependencies.

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 4: Apply Migrations
Set up the database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser
Create a superuser account to access the Django admin panel:
```bash
python manage.py createsuperuser
```

Follow the prompts to set the admin username, email, and password.

### Step 6: Run the Application with Uvicorn
Run the application using the **Uvicorn** ASGI server:
```bash
uvicorn <project_name>.asgi:application --reload
```

- Replace `<project_name>` with your Django project directory name (usually the name of your top-level project folder that contains `asgi.py`).
- The `--reload` flag automatically restarts the server when you make changes to the code.

The server will start at: `http://127.0.0.1:8000/`

---

## Project Directory Structure