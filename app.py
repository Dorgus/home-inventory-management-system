from flask import Flask, jsonify, request

app = Flask(__name__)

categories = []


@app.route("/api/categories", methods=["GET"])
def get_categories():
    return jsonify(categories)


@app.route("/api/categories", methods=["POST"])
def create_category():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Category name is required"}), 400

    category = {
        "id": len(categories) + 1,
        "name": data["name"]
    }

    categories.append(category)

    return jsonify(category), 201


if __name__ == "__main__":
    app.run(debug=True)
