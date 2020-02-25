# Flask + SQLAlchemy

# Setting Environment Variables
```
FLASK_APP=wsgi.py
```

## Setting up db locally
```
$ flask db init
$ flask db migrate -m "create tables"
$ flask db upgrade
```
### Possible errors:
```
ERROR [root] Error: Can't locate revision identified by ...
```
Make sure to delete migration folder, app.db and other migration related files

## Heroku Setup
1. Set `FLASK_APP=wsgi.py`
2. `Procfile` is instructions for heroku
3. `runtime.txt` for Python version (e.g. 3.8.1)
4. `requirements.txt`for python packages