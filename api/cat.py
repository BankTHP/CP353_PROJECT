from flask import request,jsonify,Response,current_app
from flask_restful import Resource
from flask_jwt_extended import jwt_required
import json



class CatsApi(Resource):

    def get(self):

        name = request.args.get('name')
        lifemin = request.args.get('lifemin')
        lifemax = request.args.get('lifemax')
        color = request.args.get('color')
        coat = request.args.get('coat')
        energy = request.args.get('energy')
        shedding = request.args.get('shedding')
        size = request.args.get('size')
        
        if lifemin != None and all(v is  None for v in [lifemax,name,color,coat,energy,shedding,size]): 
            data = readJson()
            cats = []
            for i in data:
                if i['LifeSpanMin'] >= float(lifemin):
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500
        
        elif name != None and all(v is  None for v in [lifemax,lifemin,color,coat,energy,shedding,size]): 
            data = readJson()
            cats = []
            for i in data:
                if name.lower() in i['Name'].lower()  :
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500

        elif lifemax != None and all(v is  None for v in [name,lifemin,color,coat,energy,shedding,size]): 
            data = readJson()
            cats = []
            for i in data:
                if i['LifeSpanMax'] <= float(lifemax):
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500

        elif color != None and all(v is  None for v in [lifemax,lifemin,name,coat,energy,shedding,size]): 
            data = readJson()
            cats = []
            for i in data:
                if  color.lower() in i['Color'].lower():
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500

        elif coat != None and all(v is  None for v in [lifemax,lifemin,color,name,energy,shedding,size]): 
            data = readJson()
            cats = []
            for i in data:
                if  coat.lower() in i['Coat'].lower():
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500

        elif energy != None and all(v is  None for v in [lifemax,lifemin,color,coat,name,shedding,size]): 
            data = readJson()
            cats = []
            for i in data:
                if  energy.lower() in i['Energy'].lower():
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500

        elif shedding != None and all(v is  None for v in [lifemax,lifemin,color,coat,energy,name,size]): 
            data = readJson()
            cats = []
            for i in data:
                if  shedding.lower() in i['Shedding'].lower():
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500

        elif size != None and all(v is  None for v in [lifemax,lifemin,color,coat,energy,shedding,name]): 
            data = readJson()
            cats = []
            for i in data:
                if  size.lower() in i['Size'].lower():
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500
        
        elif None not in (name,lifemax) and all(v is  None for v in [lifemin,color,coat,energy,shedding,size]): 
            data = readJson()
            cats = []
            for i in data:
                if  name.lower() in i['Name'].lower() and i['LifeSpanMax'] <= float(lifemax) :
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500
        
        elif None not in (name,lifemin) and all(v is  None for v in [lifemax,color,coat,energy,shedding,size]): 
            data = readJson()
            cats = []
            for i in data:
                if  name.lower() in i['Name'].lower() and i['LifeSpanMin'] >= float(lifemin) :
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500

        elif None not in (lifemax,lifemin) and all(v is  None for v in [name,color,coat,energy,shedding,size]): 
            data = readJson()
            cats = []
            for i in data:
                if  i['LifeSpanMax'] <= float(lifemax) and i['LifeSpanMin'] >= float(lifemin) :
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500
        
        elif None not in (energy,size) and all(v is  None for v in [name,color,coat,lifemin,shedding,lifemax]): 
            data = readJson()
            cats = []
            for i in data:
                if  energy.lower() in i['Energy'].lower() and size.lower() in i['Size'].lower() :
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500
        
        elif None not in (color,name) and all(v is  None for v in [lifemax,lifemin,coat,energy,shedding,size]): 
            data = readJson()
            cats = []
            for i in data:
                if  name.lower() in i['Name'].lower() and color.lower() in i['Color'].lower() :
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500

        elif None not in (coat,shedding) and all(v is  None for v in [name,color,lifemax,lifemin,energy,size]): 
            data = readJson()
            cats = []
            for i in data:
                if  i['LifeSpanMax'] <= float(lifemax) and i['LifeSpanMin'] >= float(lifemin) :
                    cats.append(i)
            if len(cats) != 0:
                return cats, 200
            else:
                return {}, 500

        else:
            return readJson(), 200

    @jwt_required() 
    def post(self):
        status = writeJson(request.get_json())
        if status == 200:
            return {"message":"Cat has been added."}, 200
        elif status == 404:
            {"message": "มีข้อมูลอยู่แล้ว."}, 404


class CatApi(Resource):      

    @jwt_required() 
    def put(self,catname):#รับ PUT
        info = request.get_json()
        status = updatejson(catname, info)
        if status == 200:
            return {
                "message": catname+"HAS BEEN UPDATED."}, 200
        elif status == 500:
            return {"message": "FAIL TO UPDATED."}, 500

    @jwt_required() 
    def delete(self,catname):
        status = deleteJson(catname)
        if status == 200:
            return {"message":catname+" has been deleted."}, 200
        elif status == 500:
            return {"message":catname+" not found."}, 500

def readJson():
    open_json_file = open('cat.json', 'r') 
    read_json_file = open_json_file.read()
    cat_data = json.loads(read_json_file)
    return cat_data

def writeJson(cat_dict):
    cats_list = readJson()
    for i in cats_list: 
        if i['Name'] == cat_dict['Name']:
            return 404
    cats_list.append(cat_dict)
    open_json_file = open('cat.json', 'w')
    json.dump(cats_list, open_json_file, indent=4) 
    return 200


def updatejson(cat_name, new_info):
    cats_list = readJson()
    if len(new_info) == 0:
        return 500
    for index, item in enumerate(cats_list):
        if item['Name'].lower() == cat_name.lower():
            for update_item in list(new_info.keys()): 
                if update_item not in list(item.keys()):
                    return 500
            cats_list[index].update(new_info)
            open_json_file = open('cat.json', 'w')
            json.dump(cats_list, open_json_file, indent=4)
            return 200
    return 500

def deleteJson(catname):
    cats_list = readJson()
    for item in cats_list:
        if item['Name'].lower() == catname.lower():
            cats_list.remove(item)
            open_json_file = open('cat.json', 'w')
            json.dump(cats_list, open_json_file, indent=4)
            return 200
    return 500
