# Django To-Do App

A simple To-Do web application built with Django that allows users to manage their daily tasks efficiently.

## Features

* User authentication (Sign Up, Login, Logout)
* Create new tasks
* Update existing tasks
* Mark tasks as completed
* Delete tasks
* Responsive user interface

## Technologies Used

* Python
* Django
* HTML
* TAILWIND CSS
* JavaScript
* POSTGRES

## Installation

1. Clone the repository.

```bash
git clone https://github.com/yourusername/todo-app.git
```

2. Navigate into the project directory.

```bash
cd todo-app
```

3. Create and activate a virtual environment.

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the project dependencies.

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project root and add the required environment variables.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

6. Apply database migrations.

```bash
python manage.py migrate
```

7. Start the development server.

```bash
python manage.py runserver
```

8. Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

## Project Structure

```
todo-app/
│
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── todo/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
└── static/
```


