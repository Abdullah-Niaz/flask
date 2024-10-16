from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


# intial data in my todo list

items = [
    {'id': 1, 'name': 'item 1', 'description': 'this is item 1'},
    {'id': 2, 'name': 'item 2', 'description': 'this is item 2'},
    {'id': 3, 'name': 'item 3', 'description': 'this is item 3'}
]


# Get: Retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


# Get the data with specific id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in items:
        if item['id'] == item_id:
            return jsonify(item)
        else:
            return jsonify({"Result Not Found with this ID"})


# Post: create a new task
@app.route('/items', methods=['POST'])
def create_item():
    if not request.method == 'POST':
        return jsonify("ERROR: item not found ")
    else:
        new_item = {
            # 'id': len(items) + 1 if items else 1,
            'id': request.json['id'],
            'name': request.json['name'],
            'description': request.json['description']
        }
        items.append(new_item)

    return jsonify(new_item)


# Put: to Update the existing product/item
@app.route("/items/<int:item_d>", methods=['PUT'])
def update_item(item_d):
    for item in items:
        if item['id'] == item_d:
            # item[id] = request.json['id']
            item['name'] = request.json['name']
            item['description'] = request.json['description']
            return jsonify(item)
        else:
            return jsonify({"Result Not Found with this ID"})


# Delete: Delte the item/product from the item list
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in items:
        if item['id'] == item_id:
            items.remove(item)
            return jsonify({"message": "Item was successfully deleted"})
        else:
            return jsonify({"message": "Item not found"})


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
