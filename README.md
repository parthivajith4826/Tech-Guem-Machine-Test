diff --git a/d:\TechGuem\README.md b/d:\TechGuem\README.md
new file mode 100644
--- /dev/null
+++ b/d:\TechGuem\README.md
@@ -0,0 +1,118 @@
+# TechGuem - Student Course Registration Portal
+
+This project is built for learning and study purposes using Django and Django REST Framework.
+
+## <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="vertical-align:middle"><path d="M4 19h16M6 16V5a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v11" stroke="#0f766e" stroke-width="2" stroke-linecap="round"/><path d="M9 8h6M9 11h6" stroke="#0f766e" stroke-width="2" stroke-linecap="round"/></svg> Tech Stack
+
+- Python 3.x
+- Django 6.0.3
+- Django REST Framework
+- SQLite
+- python-decouple
+
+## <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="vertical-align:middle"><path d="M3 7h18M3 12h18M3 17h18" stroke="#0f766e" stroke-width="2" stroke-linecap="round"/></svg> Features
+
+- Student registration
+- Student login (session-based)
+- Course list and enrollment
+- REST API for Students and Courses
+- Responsive templates with HTML/CSS/JS
+
+## <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="vertical-align:middle"><path d="M4 7h16v10H4z" stroke="#0f766e" stroke-width="2"/><path d="M8 4v3M16 4v3" stroke="#0f766e" stroke-width="2" stroke-linecap="round"/></svg> Setup
+
+1. Clone the repository
+
+```bash
+git clone <your-repo-url>
+cd TechGuem
+```
+
+2. Create and activate virtual environment
+
+Windows (PowerShell):
+
+```powershell
+python -m venv env1
+.\env1\Scripts\Activate.ps1
+```
+
+macOS/Linux:
+
+```bash
+python3 -m venv env1
+source env1/bin/activate
+```
+
+3. Install dependencies
+
+```bash
+pip install -r requirements.txt
+```
+
+4. Create `.env` file in project root
+
+```env
+SECRET_KEY=your_secret_key_here
+```
+
+5. Apply migrations
+
+```bash
+python manage.py migrate
+```
+
+6. Run development server
+
+```bash
+python manage.py runserver
+```
+
+## <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="vertical-align:middle"><path d="M12 3l8 4v10l-8 4-8-4V7z" stroke="#0f766e" stroke-width="2"/><path d="M12 7v10M8 9l8 4" stroke="#0f766e" stroke-width="2" stroke-linecap="round"/></svg> Web Routes
+
+Base URL: `http://127.0.0.1:8000/`
+
+- `GET /` -> Home page
+- `GET /register/` -> Register page
+- `POST /register/` -> Create student
+- `GET /login/` -> Login page
+- `POST /login/` -> Login student
+- `GET /courses/` -> Courses page
+- `GET /register-course/<int:pk>` -> Register selected course for logged-in student
+- `GET /logout/` -> Logout student
+- `GET /admin/` -> Django admin
+
+## <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="vertical-align:middle"><path d="M7 8h10M7 12h10M7 16h6" stroke="#0f766e" stroke-width="2" stroke-linecap="round"/><rect x="3" y="4" width="18" height="16" rx="2" stroke="#0f766e" stroke-width="2"/></svg> API Endpoints
+
+Base API URL: `http://127.0.0.1:8000/api/v1/`
+
+### Students API
+
+- `GET /api/v1/students/` -> List all students
+- `POST /api/v1/students/` -> Create a student
+- `GET /api/v1/students/<int:pk>/` -> Retrieve one student
+- `PUT /api/v1/students/<int:pk>/` -> Update full student record
+- `PATCH /api/v1/students/<int:pk>/` -> Partial update student
+- `DELETE /api/v1/students/<int:pk>/` -> Delete student
+
+### Courses API
+
+- `GET /api/v1/courses/` -> List all courses
+- `POST /api/v1/courses/` -> Create a course
+- `GET /api/v1/course/<int:pk>/` -> Retrieve one course
+- `PUT /api/v1/course/<int:pk>/` -> Update full course record
+- `PATCH /api/v1/course/<int:pk>/` -> Partial update course
+- `DELETE /api/v1/course/<int:pk>/` -> Delete course
+
+## <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="vertical-align:middle"><path d="M12 8v5l3 2" stroke="#0f766e" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="12" r="9" stroke="#0f766e" stroke-width="2"/></svg> Useful Commands
+
+```bash
+python manage.py check
+python manage.py makemigrations
+python manage.py migrate
+python manage.py createsuperuser
+python manage.py runserver
+```
+
+## <svg width="18" height="18" viewBox="0 0 24 24" fill="none" style="vertical-align:middle"><path d="M12 9v4M12 17h.01" stroke="#b91c1c" stroke-width="2" stroke-linecap="round"/><path d="M10.3 3.84 1.82 18a2 2 0 0 0 1.72 3h16.92a2 2 0 0 0 1.72-3L13.7 3.84a2 2 0 0 0-3.4 0Z" stroke="#b91c1c" stroke-width="2"/></svg> Note
+
+This project is developed only for study purposes.
