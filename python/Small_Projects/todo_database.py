from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///items.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "done": self.done}


# create tables

with app.app_context():
    db.create_all()

# CRUD routes
# select all


@app.get("/items")
def get_items():
    items = Item.query.all()
    return jsonify([i.to_dict() for i in items]), 200

# select one


@app.get("/items/<int:item_id>")
def get_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"Error": "Item not found"}), 404
    return jsonify(item.to_dict()), 200

# create


@app.post("/items")
def create_item():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"Error": "Invalid input"}), 400
    # Get the value for the key 'done' if it exists; otherwise, use False by default.
    new_item = Item(name=data["name"], done=data.get("done", False))
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201


# Update

@app.put("/items/<int:item_id>")
def update_item(item_id):
    data = request.get_json()
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"Error: item not found"}), 404

    # If the user has provided a new value for name in the JSON request, update it.Otherwise, keep the current value as-is.
    item.name = data.get("name", item.name)
    item.done = data.get("done", item.done)
    db.session.commit()
    return jsonify(item.to_dict()), 200

# Delete


@app.delete("/items/<int:item_id>")
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"Error: item not found"}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "item successfully deleted"}), 200


# Run server
if __name__ == "__main__":
    app.run(debug=True)
