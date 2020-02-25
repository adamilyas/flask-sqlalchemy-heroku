from application import app, db
from application.models import User, Task
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

# task
@app.route("/addTaskToUser/<_username>/<_taskname>")
def add_task_to_user(_username, _taskname):

    try:
        found_user = User.query.filter_by(username=_username).first()

        if found_user is None:
            response_message = {"message": f'Username: {_username} not found'}
            response_status = 400
        else:
            user_id = found_user.id
            task = Task(task_name=_taskname, user_id=user_id)

            db.session.add(task)
            db.session.commit()
            response_message = {"message": f'Added: {task}'}
            response_status = 200

        return jsonify(response_message), response_status
    except Exception as e:
        app.logger.info(e.with_traceback())
        return "error", 500

@app.route("/getTaskByUserName/<_username>")
def get_task_by_user_name(_username):
    app.logger.info(f'Received user_name: {_username}')
    try:
        # get user id of the user_name
        found_user = User.query.filter_by(username=_username).first()

        if found_user is None:
            app.logger.info(f'UserId NOT FOUND for username: {_username}')

            response_message = {"message": f'Username: {_username} not found'}
            response_status = 400
        else:
            user_id = found_user.id
            app.logger.info(f'UserId: {user_id} for username: {_username}')

            tasks = Task.query.filter_by(user_id=user_id)
            ls = [{"task_name": task.task_name, "status": task.status} for task in tasks]
            response_message = {"message": "Search Success", "data": ls}
            response_status = 200

        return jsonify(response_message), 200
    except Exception as e:
        app.logger.info(e)
        return "error", 500