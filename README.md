# Blog API - Hobby Project

A Blog API using the full set of Django REST Framework features. It have users, permissions, and allow for full CRUD (Create-Read-Update-Delete) functionality and Support Swagger API Documentation tool. 
        UserList           |           PostList
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/87778419/168694578-40f79af8-4a24-4685-a271-f9beb5bd56d0.png)  |  ![](https://user-images.githubusercontent.com/87778419/168694670-6a8616f3-e495-4775-815a-28a26658ecb8.png)


## 📖 Installation
To start, Install Python, pipenv then clone the repo to your local computer and change into the proper directory.
```
$ git clone https://github.com/cute-bunny917/bookstore.git
$ cd blogapi
$ pipenv install
$ pipenv shell
$ python manage.py createsuperuser
$ python manage.py runserver
open http://127.0.0.1:8000/swagger/  to work with API Documentation tool(swagger)
open http://127.0.0.1:8000/api/v1/  to work with API.
```
<img src="https://user-images.githubusercontent.com/87778419/168694793-26a2f1c4-c3c8-4231-aa30-c7ed7e70872f.png">
## 🚀 Features

- Django 4.0.4 & Python 3.8
- Django REST Framework 3.13.0
- Install via [Pip](https://pypi.org/project/pip/), [Pipenv](https://pypi.org/project/pipenv/)
- User log in/out, sign up, password reset endpoint via [dj-rest-auth](https://github.com/iMerica/dj-rest-auth) and [django-allauth](https://github.com/pennersr/django-allauth)
- Pyyaml , Uritemplate & Drf-yasg to generate API Documentation tool.

