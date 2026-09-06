# tourbazz_bd

This is an intelligent tour manager built with Django and SQLite.

## Requirements

- Windows
- Python 3.11.x (the project uses Django 5.2 LTS)
- SQLite (included with Python)

The verified Python dependencies are listed in `requirements.txt`.

## Setup

Open PowerShell in the project directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade "pip<25.1"
python -m pip install -r requirements.txt
```

If `python` is not available after installing Python, use the Python 3.11 executable directly when creating the environment:

```powershell
& "$env:LocalAppData\Programs\Python\Python311\python.exe" -m venv .venv
```

PowerShell may block virtual-environment activation. Allow it for the current user, then activate again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

## Database

The repository includes `db.sqlite3`. Apply any pending migrations with:

```powershell
python manage.py migrate
```

Create an administrator account for `/admin/` when needed:

```powershell
python manage.py createsuperuser
```

## Run the development server

```powershell
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a browser. The admin site is available at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

Stop the server with `Ctrl+C`.

## Validation commands

```powershell
python manage.py check
python manage.py test
python manage.py showmigrations
```

The current repository has no implemented tests, so `manage.py test` currently reports zero tests.

## Review notes

- The deployment target uses Django 5.2 LTS with Python 3.11. `setuptools` is included for compatibility with packages that still use its `distutils` shim.
- `DEBUG` is enabled and the secret key is stored in `tourbazz_bd/settings.py`; do not use these settings for production.
- `ALLOWED_HOSTS` is empty, which is suitable for local development but must be configured for deployment.
- SQLite and the existing migrations are ready: all migrations were applied and no migration operations are pending.
- The home page was verified locally with an HTTP 200 response after installation.
