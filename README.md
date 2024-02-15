# Environment Setup
1. **Create an enviroment**

```bash
    virtualenv .venv
```

2. **Activate environment**

```bash
    source .venv/bin/activate
```
3. **Setup .gitignore**

```bash
    echo ".*venv*/" > .gitignore
```
4. **Install django**

```bash 
    pip install django
```
5. **Setup requirements.txt**

```bash
    pip freeze > requirements.txt
```
- For every package installed during the project, run this command to save dependencies with their versions.

# Django Project Setup

6. **Create a django project**

```bash
    django-admin startproject <project-name> <path>
```
7. **Create django app**

```bash
    python manage.py startapp <app-name>
```
8. **Register app in `INSTALLED_APPS` in `settings.py` file**

9. **Update base `urls.py` for regsitered app**

# Database Configuration

9. **Define Models**

- Define your database models in the <app-name>/`models.py` file.

10. **Migrate Models to Database**

```bash
    python manage.py makemigrations
```
```bash
    python manage.py migrate
```

# Views

11. **Create a `views/` folder inside your app**
12. **`views/` folder should contain all the views for the app.**
13. **Update app `urls.py` to register your views**
