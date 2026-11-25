# YaMovies

Educational project — an online cinema with a movie catalog, user authentication, and a review system. Built with Django (MVT architecture).

**Stack:** Python, Django, SQLite, HTML, CSS.

## Requirements

- Python 3.10+
- Git
- Terminal / Command Prompt

## Getting Started

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate it

Windows:
```bash
.venv\Scripts\activate
```

macOS / Linux:
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create superuser

```bash
python manage.py createsuperuser
```

### 6. Run

```bash
python manage.py runserver
```

Address: http://localhost:8000