from flask import request,jsonify,Response,current_app
from flask_restful import Resource
from flask_jwt_extended import jwt_required
import json


class CatApi(Resource):

    def get(self):
        return readJson(),200

    @jwt_required() 
    def post(self):
        status = write_food_json(request.get_json())
        if status == 200:
            return {"message":"Cat has been added."}, 200
    @jwt_required()
    def put(self,catname):#รับ PUT
        print(catname)
        info = request.get_json()
        print(info)
        # status = updatejson(catname, info)
        # if status == 200:
        #     return {
        #         "message":"Cat HAS BEEN UPDATED."
        #         }, 200
        # elif status == 500:
        #     return {"message": "FAIL TO UPDATED."}, 500

def readJson():
    open_json_file = open('cat.json', 'r') 
    read_json_file = open_json_file.read()
    animal_data = json.loads(read_json_file)
    return animal_data

def write_food_json(animal_dict):
    foods_list = readJson()
    foods_list.append(animal_dict)
    open_json_file = open('cat.json', 'w')
    json.dump(foods_list, open_json_file, indent=4) 
    return 200

def updatejson(food_name, new_info):
    foods_list = readJson()
    if len(new_info) == 0:
        return 500
    for index, item in enumerate(foods_list):
        if item['Name'].lower() == food_name.lower():
            for update_item in list(new_info.keys()): 
                if update_item not in list(item.keys()):
                    return 500
            foods_list[index].update(new_info)
            open_json_file = open('cat.json', 'w')
            json.dump(foods_list, open_json_file, indent=4)
            return 200
    return 500