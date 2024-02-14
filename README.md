# Environment Setup
1 **Create an enviroment**

```bash
    virtualenv .venv
```

2 **Activate environment**

```bash
    source .venv/bin/activate
```
3 **Setup .gitignore**

```bash
    echo ".*venv*/" > .gitignore
```
4 **Install django**

```bash 
    pip install django
```

# Django Project Setup

5 **Create a django project**

```bash
    django-admin startproject <project-name> <path>
```
6 **Create django app**

```bash
    python manage.py startapp <app-name>
```

# Database Configuration

7 **Define Models**

- Define your database models in the <app-name>/models.py file.

8 **Migrate Models to Database**
```bash
    python manage.py makemigrations
```
```bash
    python manage.py migrate
```