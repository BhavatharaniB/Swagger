from flask import Flask, jsonify, request


app = Flask(__name__)  # creating flask app

data = [{'message': "Hello"}, {'message': "welcome"}]


@app.route('/GET', methods=['GET'])
def get():
    return jsonify({"message": "hi"})


@app.route('/POST', methods=['POST'])
def post():
    new_data = request.get_json()
    print(new_data)
    data.append(new_data)
    print(data)
    return "Post method executed"


@app.route('/PUT/<string:message>', methods=['PUT'])
def put(message):
    new_data = request.get_json()
    print(new_data)
    for i, m in enumerate(data):
        if m['message'] == message:
            data[i] = new_data
    print(data)
    return "Put method executed"


@app.route('/DELETE/<string:message>', methods=['DELETE'])
def delete(message):
    for i, q in enumerate(data):
        if q['message'] == message:
            del data[i]
        print(data)
    return "Delete method executed"


@app.route('/PATCH/<string:message>', methods=['PATCH'])
def patch(message):
    new_data = request.get_json()
    print(new_data)
    for i, m in enumerate(data):
        if m['message'] == message:
            data[i] = new_data
    print(data)
    return "Patch method executed"


if __name__ == "__main__":
        app.run()
