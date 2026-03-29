from flask import Flask, request, jsonify
from data import inventory

app = Flask(__name__)


def generate_id():
    if len(inventory) == 0:
        return 1
    return inventory[-1]["id"] + 1


@app.route("/")
def home():
    return jsonify({"message": "Inventory API is working"})


@app.route("/inventory", methods=["GET"])
def get_items():
    return jsonify(inventory), 200


@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_one_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404


@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Please send JSON data"}), 400

    if "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    new_item = {
        "id": generate_id(),
        "name": data["name"],
        "price": data.get("price", 0),
        "stock": data.get("stock", 0)
    }

    inventory.append(new_item)
    return jsonify(new_item), 201


@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            data = request.get_json()

            if not data:
                return jsonify({"error": "Please send JSON data"}), 400

            item["name"] = data.get("name", item["name"])
            item["price"] = data.get("price", item["price"])
            item["stock"] = data.get("stock", item["stock"])

            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Item deleted"}), 200

    return jsonify({"error": "Item not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)