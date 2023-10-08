# Development tools

## Backend

### PostgreSQL

We are using PostgreSQL for persistent storage.

https://www.postgresql.org/

### Django

At the core of the backend we run the Django framework. A popular framework was chosen 
to lower the barrier of creating a plugin. We also looked for a batteries included, 
simple, and proven framework. Django was the obvious choice.

https://www.djangoproject.com

### Django REST framework

To quickly create endpoints, handle authentication, object serialization, validation, 
and do many more things we use Django REST Framework. You will find it at the base or
every endpoint.

https://www.django-rest-framework.org/

### pytest

We use pytest to easily and automatically test all the python code. Most of the backend
code is covered with tests and we like to keep it that way! The code is also tested
in the [continuous integration pipeline](./code-quality.md). It can also be tested 
manually in the development environment.
Execute  the following command.

```
$ make test
```

https://docs.pytest.org/en/latest/contents.html

### Flake8

Flake8 makes it easy to enforce our python code style. Execute the following command. If all the code meets the standards you should not see any output.

```
$ make lint
```

https://flake8.pycqa.org/en/latest/

### Black 

Black auto formats all of our python code into one opinionated consistent style. The 
goal being to reduce and hopefully eliminate the need to worry about formatting whilst
writing and reviewing code.

https://black.readthedocs.io/en/stable/index.html

### ItsDangerous

In order to safely share sensitive data like password reset tokens we use a proven
library called ItsDangerous.

https://itsdangerous.palletsprojects.com/en/1.1.x/

### DRF spectacular

Having up to date API documentation and having it in the OpenAPI specification format 
is a must. To avoid mistakes, the contents are close to the code and are automated as 
much as possible. DRF Spectacular offers all of this!

https://pypi.org/project/drf-spectacular/

### MJML

In order to simplify the process of creating HTML emails we use MJML. This tool makes
it easy to create responsive emails that work with most email clients. This might seem
a bit like over engineering to use this for only the password forgot email, but more
complicated emails are going to be added in the future and we wanted to have a solid 
base. 

https://mjml.io/

