from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Build REST API", "completed": False}
]

# Generate unique task IDs
next_id = 3


@app.route("/")
def home():
    return jsonify({
        "message": "Python Task Manager API is running"
    })


# GET - All tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


# GET - Single task
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task), 200

    return jsonify({
        "error": "Task not found"
    }), 404


# POST - Create a task
@app.route("/tasks", methods=["POST"])
def add_task():
    global next_id

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    if "title" not in data:
        return jsonify({
            "error": "Task title is required"
        }), 400

    if not isinstance(data["title"], str) or not data["title"].strip():
        return jsonify({
            "error": "Task title cannot be empty"
        }), 400

    new_task = {
        "id": next_id,
        "title": data["title"].strip(),
        "completed": False
    }

    tasks.append(new_task)
    next_id += 1

    return jsonify(new_task), 201


# PUT - Update a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    for task in tasks:
        if task["id"] == task_id:

            if "title" in data:
                if not isinstance(data["title"], str) or not data["title"].strip():
                    return jsonify({
                        "error": "Task title cannot be empty"
                    }), 400

                task["title"] = data["title"].strip()

            if "completed" in data:
                if not isinstance(data["completed"], bool):
                    return jsonify({
                        "error": "Completed must be true or false"
                    }), 400

                task["completed"] = data["completed"]

            return jsonify(task), 200

    return jsonify({
        "error": "Task not found"
    }), 404


# DELETE - Delete a task
@app.route("/tasks/<int:task_id>",