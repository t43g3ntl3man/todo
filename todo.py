from flask import Flask, request, url_for, render_template, jsonify, json, abort
from flask_pymongo import PyMongo

todo = Flask(__name__)
todo.config['MONGO_DBNAME'] = 'todo_db'
todo.config['MONGO_URI'] = 'mongodb://admin:admin123@ds123012.mlab.com:23012/todo_db'

mongo = PyMongo(todo)

@todo.route("/todo/api/v1.0/tasks", methods = ['GET'])
def task_get():
	todo = {}
	todoDb = mongo.db.todos
	todoCount = todoDb.find({}).count();
    	if todoCount == 0:
    		return "ToDo list is empty"
		abort(500)
	else:
		todos = todoDb.find({})
		a = 0
		for a in todos:
			todo[a["id"]] = {
			"id": a["id"],
			"title": a["title"],
			"description": a["description"],
			"done": bool(a["done"])
			}
		
	return (jsonify(todo))

@todo.route("/todo/api/v1.0/tasks", methods = ["POST"])
def task_add():
	title = request.json["title"]
	description = request.json.get('description', '')
	done = bool(request.json["done"])
	todoDB = mongo.db.todos
	todoCount = todoDB.find({}).count()
	todoDB.insert({
	        "id": todoCount + 1,
	        "title": title,
	        "description": description,
	        "done": done
   	 })
	
	return "ToDo list updated"

@todo.route("/todo/api/v1.0/tasks/<int:idd>", methods = ['GET'])
def get_task(idd):
	todo = {}
	todoDB = mongo.db.todos
	task = todoDB.find({"id": idd})
	todoCount = todoDB.find({}).count();
	if todoCount == 0:
    		return "ToDo list is empty"
		abort(500)
	for a in task:
		todo[a["id"]] = {
		"id": a["id"],
	        "title": a["title"],
	        "description": a["description"],
	        "done": bool(a["done"])
	        }
	
	return (jsonify(todo))

@todo.route("/todo/api/v1.0/tasks/<int:idd>", methods = ["PUT"])
def edit_task(idd):
	title = request.json["title"]
	description = request.json.get('description', '')
	done = bool(request.json["done"])
	todoDB = mongo.db.todos
	toupdate = todoDB.find({"id" : idd})
	title = request.json.get("title", toupdate[0]["title"])
 	description = request.json.get('description', toupdate[0]["description"])
	done = bool(request.json.get("done", toupdate[0]["done"]))
	update = todoDB.update_one(
        { "id": idd},
        {
            '$set' : {
                "title": title,
                "description": description,
                "done": done
            }
        }
        )
	return "ToDo list is updated"

@todo.route("/todo/api/v1.0/tasks/<int:idd>", methods = ['DELETE'])
def delete_task(idd):
	todoDB = mongo.db.todos
	todoDB.delete_one({"id": idd})
	return "Todo list is updated"

todo.run(debug=True, port=5000)
