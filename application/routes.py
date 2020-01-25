from application import app, db
from application.models import User
from flask import jsonify, Response

@app.route("/_health")
def check_health():
    return "normal"

@app.route("/addUser/<_username>/<_email>")
def add_user(_username, _email):
    u = User(username=_username, email=_email)
    try:
        db.session.add(u)
        db.session.commit()
        user_added = {"username": u.username, "email": u.email}
        return jsonify(user_added), 200
    except:
        return "error", 500

@app.route("/findAll")
def find_all():
    result = User.query.all()
    ls = [{"username": user.username, "email": user.email} for user in result ]
    return jsonify(ls)

@app.route("/deleteAll")
def delete_all():
    try:
        num_rows_deleted = db.session.query(User).delete()
        db.session.commit()
        response_body = {"message": "ok", "count": num_rows_deleted}
        return  jsonify(response_body), 200
    except Exception as e:
        db.session.rollback()
        return {"message": e}, 500