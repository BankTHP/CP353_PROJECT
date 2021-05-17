import json,requests,jsonify
url = "http://127.0.0.1:5000/cat"
data= requests.request("GET", url).json()
print(jsonify(url))