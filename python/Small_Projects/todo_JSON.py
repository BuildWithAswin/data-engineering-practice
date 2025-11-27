from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

TASKS_FILE = "tasks.json"

# Helper function - read


def read_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

#  - write


def write_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# CRUD routes

# read all


@app.route("/task", methods=["GET"])
def get_items():
    tasks = read_tasks()
    return jsonify(tasks), 200


# read one

@app.route("/task/<int:task_id>", methods=["GET"])
def get_item(task_id):
    tasks = read_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"Error": "Task not found"})
    return jsonify(task), 200

# post


@app.post("/task")
def create_task():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"Error": "Inalid input"}), 400
    tasks = read_tasks()
    new_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = {
        "id": new_id,
        "name": data["name"],
        "done": data.get("done", False)
    }
    tasks.append(new_task)
    write_tasks(tasks)
    return jsonify(new_task), 201

# update


@app.put("/task/<int:task_id>")
def update_task(task_id):
    data = request.get_json()
    tasks = read_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"Error": "Invalid input"}), 404

    task["name"] = data.get("name", task["name"])
    task["done"] = data.get("done", task["done"])

    write_tasks(tasks)
    return jsonify(task), 200

# delete


@app.delete("/task/<int:task_id>")
def delete_task(task_id):
    tasks = read_tasks()
    updated_tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        return jsonify({"Error": "Task not found"}), 404
    write_tasks(updated_tasks)
    return jsonify({"message": "task successfully deleted!"}), 200


# run the app
if __name__ == "__main__":
    app.run(debug=True)
