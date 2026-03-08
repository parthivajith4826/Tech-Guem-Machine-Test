# Student Course Registration Portal

This project is built for learning and study purposes using Django and Django REST Framework.

## ◈ Tech Stack

- Python 3.x
- Django 6.0.3
- Django REST Framework
- SQLite
- python-decouple

## ◈ Features

- Student registration
- Student login (session-based)
- Course list and enrollment
- REST API for Students and Courses
- Responsive templates with HTML/CSS/JS

## ◈ Setup

1. Clone the repository
``````````bash
git clone <your-repo-url>
cd TechGuem
\```

2. Create and activate virtual environment

**Windows (PowerShell):**
`````````powershell
python -m venv env1
.\env1\Scripts\Activate.ps1
\```

**macOS/Linux:**
````````bash
python3 -m venv env1
source env1/bin/activate
\```

3. Install dependencies
```````bash
pip install -r requirements.txt
\```

4. Create `.env` file in project root
``````env
SECRET_KEY=your_secret_key_here
\```

5. Apply migrations
`````bash
python manage.py migrate
\```

6. Run development server
````bash
python manage.py runserver
\```

## ◈ Web Routes

Base URL: `http://127.0.0.1:8000/`

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Home page |
| GET | `/register/` | Register page |
| POST | `/register/` | Create student |
| GET | `/login/` | Login page |
| POST | `/login/` | Login student |
| GET | `/courses/` | Courses page |
| GET | `/register-course/<int:pk>` | Register course for logged-in student |
| GET | `/logout/` | Logout student |
| GET | `/admin/` | Django admin |

## ◈ API Endpoints

Base API URL: `http://127.0.0.1:8000/api/v1/`

### Students

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/students/` | List all students |
| POST | `/api/v1/students/` | Create a student |
| GET | `/api/v1/students/<int:pk>/` | Retrieve one student |
| PUT | `/api/v1/students/<int:pk>/` | Update full student record |
| PATCH | `/api/v1/students/<int:pk>/` | Partial update student |
| DELETE | `/api/v1/students/<int:pk>/` | Delete student |

### Courses

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/courses/` | List all courses |
| POST | `/api/v1/courses/` | Create a course |
| GET | `/api/v1/course/<int:pk>/` | Retrieve one course |
| PUT | `/api/v1/course/<int:pk>/` | Update full course record |
| PATCH | `/api/v1/course/<int:pk>/` | Partial update course |
| DELETE | `/api/v1/course/<int:pk>/` | Delete course |

## ◈ Useful Commands
```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
\```

## ▲ Note

This project is developed only for study purposes.
