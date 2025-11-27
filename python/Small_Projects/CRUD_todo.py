from flask import Flask, jsonify, request
app = Flask(__name__)
# In-memory storage
items = [
    {"id": 1, "name": "Buy grocerries", "done": False},
    {"id": 2, "name": "wash utensils", "done": True},
]


# Get all item
@app.get("/items")
def get_items():
    return jsonify(items)

# Read one item


@app.get("/items/<int:item_id>")
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 400


# Create


@app.post("/items")
def create_item():
    data = request.get_json()  # reading data that goes into the api
    if not data or "name" not in data:
        return jsonify({"Error": "Missing item name"}), 400
    new_item = {
        # below line is a list comprehension - create a list of id's from items , slect max of it and add 1 , if no elements then 0
        "id": max([i["id"] for i in items], default=0) + 1,
        "name": data["name"],
        "done": False
    }
    items.append(new_item)
    return jsonify(new_item), 201

# Update


@app.put("/items/<int:item_id>")
def update_item(item_id):
    data = request.get_json()
    for item in items:
        if item["id"] == item_id:
            item["name"] = data.get("name", item["name"])
            item["done"] = data.get("done", item["done"])
            return jsonify(item)
    return jsonify({"error: Item not found"}), 404

# Delete


@app.delete("/items/<int:item_id>")
def delete_item(item_id):
    global items
    items = [i for i in items if i["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
