# POC

## Project setup
Prepare [Virtualenv](https://virtualenv.pypa.io/en/latest/installation/) 

```bash
virtualenv -p pyton3 venv
. venv/bin/activate
(venv) pip install -r requirements.txt
(venv) cd poc_simple
(venv) python manage.py migrate
```

## Run server
```bash
(venv) python manage.py runserver localhost:8000
```