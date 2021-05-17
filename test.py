import json
def readJson():
    open_json_file = open('faculty.json', 'r',encoding="utf8") 
    read_json_file = open_json_file.read()
    cat_data = json.loads(read_json_file)
    return cat_data
test = readJson()
listname = []
for i in range(len(test)) :
    listname.append(str(test[i]['lon'])+",")
for i in range(len(listname)) :
    print(listname[i])