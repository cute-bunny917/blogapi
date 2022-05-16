# Blog API - Hobby Project

A Blog API using the full set of Django REST Framework features. It have users, permissions, and allow for full CRUD (Create-Read-Update-Delete) functionality and Support Swagger API Documentation tool. 

## 📖 Installation
To start,Install Python, pipenv then clone the repo to your local computer and change into the proper directory.
```
$ git clone https://github.com/cute-bunny917/bookstore.git
$ cd blogapi
$ pipenv install
$ pipenv shell
$ python manage.py runserver
open http://127.0.0.1:8000/swagger/  for API Documentation tool
open http://127.0.0.1:8000/api/v1/ to work with API.
```

## 🚀 Features

- Django 4.0.4 & Python 3.8
- Django REST Framework 3.13.0
- Install via [Pip](https://pypi.org/project/pip/), [Pipenv](https://pypi.org/project/pipenv/)
- User log in/out, sign up, password reset endpoint via [dj-rest-auth] and [django-allauth](https://github.com/pennersr/django-allauth)
- Pyyaml & Uritemplate & Drf-yasg to generate API Documentation tool.
