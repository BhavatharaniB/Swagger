# importing required packages
from flask import Flask
from flask import request
from flasgger import Swagger
from bson import json_util
import logging
import pymongo

# creating flask app
app = Flask(__name__)
Swagger(app)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["http"]
mycol = mydb["messages"]
logging.basicConfig(filename='myapp.log', level=logging.DEBUG)


@app.route('/get_details', methods=['GET'])
def get():
    """
        Documentation for flask application
        ---
        tags:
          - Flask application with RestAPI
        parameters:
          - name: name
            in: query
            type: string
            required: true
            description: message
        definitions:
            name:
                type: object
        responses:
          500:
            description: Error cannot get the message..
          200:
            description: Success
    """

    try:
        name = request.args.get('name')
        if name:
            new_data = {"message": name}
            data_list = mycol.find_one(new_data)
        else:
            new_data = dict()
            data_list = mycol.find(new_data)
        if data_list:
            logging.debug(json_util.dumps(data_list))
            message = "Data retrieved successfully"
            return json_util.dumps({"message": message, "status": "success", "data": data_list})
        else:
            message1 = "No data matches query"
            return json_util.dumps({"message": message1, "status": "success", "data": []})
    except Exception as e:
        print(e)
        # return json_util.dumps({"message": "failed to fetch data", "status": "error"})
        logging.error("Exception occurred", exc_info=True)
    finally:
        logging.info('Finished')


@app.route('/post', methods=['POST'])
def post():
    """
            Documentation for flask application
            ---
            tags:
              - Flask application with RestAPI
            parameters:
              - name: message
                in: body
                type: application/json
                required: false
            definitions:
                message:
                  type: object
            responses:
              500:
                description: Error cannot post the message..
              200:
                description: Successfully posted..
    """
    try:
        logging.info('Post method started')
        new_data = request.get_json()
        print(new_data)
        logging.info(new_data)
        mycol.insert(new_data)
        # print all the details:
        for x in mycol.find():
            print(x)
        logging.info('Post method finished')
        return "posted successfully"
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)


@app.route('/put', methods=['PUT'])
def put():
    """
               Documentation for flask application
               ---
               tags:
                 - Flask application with RestAPI
               parameters:
                 - name: new_data
                   in: body
                   type: application/json
                   required: false
               definitions:
                   new_data:
                       type: object
               responses:
                 500:
                   description: Error cannot update the message..
                 200:
                   description: Successfully updated..
    """
    try:
        logging.info('Put method started')
        new_data = request.get_json()
        data_old = new_data.get("old")
        data_new = new_data.get("new")
        data_new1 = {"$set": data_new}
        print(type(new_data))
        logging.info(new_data)
        mycol.update_one(data_old, data_new1)
        for x in mycol.find():
            print(x)
        logging.info('Put method finished')
        return "Put method executed"
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)


@app.route('/delete', methods=['DELETE'])
def delete():
    """
                   Documentation for flask application
                   ---
                   tags:
                     - Flask application with RestAPI
                   parameters:
                     - name: new_data
                       in: body
                       type: application/json
                       required: false
                   definitions:
                       new_data:
                           type: object
                   responses:
                     500:
                       description: Error cannot delete the message..
                     200:
                       description: Successfully deleted..
    """
    try:
        logging.info('Delete method started')
        new_data = request.get_json()
        # print(new_data)
        logging.info(new_data)
        mycol.delete_one(new_data)
        for x in mycol.find():
            print(x)
        logging.info('Delete method finished')
        return "Delete method executed"
    except Exception as e:
        # logging.error(str(e))
        logging.error("Exception occurred", exc_info=True)


if __name__ == "__main__":
    app.run(debug=True)
