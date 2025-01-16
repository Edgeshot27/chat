# ChatApp

ChatApp is a web-based application designed for real-time messaging and communication. This Django-powered project includes user authentication, responsive design, and interactive features.

## Features
- User Authentication System (Signup, Login, and Logout).
- Responsive design for various devices with dynamic scaling based on screen size.
- Dashboard, Messaging, Settings, and Help functionality.
- Styled with modern CSS for an appealing user interface.

## Requirements
To run this project locally, ensure you have the following installed:
- Python 3.10 or above
- Django
- Redis (for any asynchronous tasks or caching if used in the future)

## Installation Instructions
Follow these steps to set up the project on your local machine:

### Step 1: Clone the Repository
```bash
git clone <your-repository-url>
cd <project-directory>
```

### Step 2: Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
Install all necessary packages using `pip`.

```bash
pip install -r requirements.txt
```

### Step 4: Configure the Database
If the project uses a database, apply migrations to set up the database schema.

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Admin User)
To access the admin panel, create a superuser:
```bash
python manage.py createsuperuser
```

Follow the prompts to set up admin credentials.

### Step 6: Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/` by default. Open this URL in your web browser to access the app.

---

## Project Directory Structure
Here's a general overview of the project structure:
