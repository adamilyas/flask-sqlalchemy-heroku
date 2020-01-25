# Flask + SQLAlchemy

# Setting Environment Variables
```
FLASK_APP=wsgi.py
```

## Setting up db locally
```
$ cd server
$ flask db init
$ flask db migrate -m "users table"
$ flask db upgrade
```

## Heroku Setup
1. Set `FLASK_APP=wsgi.py`
2. `Procfile` is instructions for heroku
3. `runtime.txt` for Python version (e.g. 3.8.1)
4. `requirements.txt`for python packages