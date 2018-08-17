from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/cr00k3dman/Desktop/todo.db', 'crud.sqlite')
db = SQLAlchemy(app)


class User(db.Model):
    idd = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(120), unique=True)

    def __init__(self, idd, title, description):
        self.title = title
        self.description = description








# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']
    
    new_user = User(username, email)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)


# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username = username

    db.session.commit()
    return user_schema.jsonify(user)


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)
