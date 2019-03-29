# importing required packages
from flask import Flask
from flask import request
from bson import json_util
import pymongo

# creating flask app
app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["http"]
mycol = mydb["messages"]


@app.route('/get_details', methods=['GET'])
def get():
    try:
        name = request.args.get('name')
        if name:
            new_data = {"message": name}
            data_list = mycol.find_one(new_data)
        else:
            new_data = dict()
            data_list = mycol.find(new_data)
        if data_list:
            message = "Data retrieved successfully"
            return json_util.dumps({"message": message, "status": "success", "data": data_list})
        else:
            message = "No data matches query"
            return json_util.dumps({"message": message, "status": "success", "data": []})
    except Exception as e:
        print(e)
        return json_util.dumps({"message": "failed to fetch data", "status": "error"})


@app.route('/post', methods=['POST'])
def post():
    new_data = request.get_json()
    print(new_data)
    mycol.insert(new_data)
    # print all the details:
    for x in mycol.find():
        print(x)
    return "posted successfully"


@app.route('/put', methods=['PUT'])
def put():
    new_data = request.get_json()
    data_old = new_data.get("old")
    data_new = new_data.get("new")
    print(type(new_data))
    mycol.update_one(data_old, data_new)
    for x in mycol.find():
        print(x)
    return "Put method executed"


@app.route('/delete', methods=['DELETE'])
def delete():
    new_data = request.get_json()
    print(new_data)
    mycol.delete_one(new_data)
    for x in mycol.find():
        print(x)
    return "Delete method executed"


if __name__ == "__main__":
    app.run()
