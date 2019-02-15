# restful-ws-drf

Simple implementation of a RESTful API using Django Rest Framework with ModelViewSet and CustomView


## Instalation

With conda

```shell
conda create --name venv --file requirements.txt
```

## How to run the server

First set up your env by copying .env.example to .env and giving the values of the variables

Than create your database and follow the following steps:
```shell
conda activate venv
python manage.py migrate
python manage.py runserver
```
Then access http://127.0.0.1:8000/api/

## Links

I've followed the following article for good practices


- https://hackernoon.com/restful-api-design-step-by-step-guide-2f2c9f9fcdbf
