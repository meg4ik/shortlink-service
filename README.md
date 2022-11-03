 Shortlink service

## About Project
 Django link shortening project. Test task for 'АНЦ' company. Has been implemented by Pavlo Ryndin.


### Basics

1. Fork/Clone
1. Activate a virtualenv
1. Install the requirements


### Create DB

Do migration

```sh
$ python manage.py migrate
```

## Run the Application

```sh
$ python manage.py runserver
```

Access the application at the address [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Admin manage

```sh
$ python manage.py createsuperuser
```

## Accessible urls

```sh
'/'
'/list'
'/redirect/<shortlink>'
'/login'
'/logout'
'/signup'
'/admin'
'/api/links'
'/api/links/create'
```