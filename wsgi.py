from application import app, db
from application import models, routes
# The Web Server Gateway Interface (WSGI)

if __name__ == "__main__":
    app.run(debug=True)