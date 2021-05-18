import json
data = json.load(open('faculty.json',encoding="utf8"))
listcheck = []
for i in range(len(data)):
    listcheck.append(data[i]['facultyName'])
for i in range(len(listcheck)):
    print('"'+listcheck[i]+'",')

