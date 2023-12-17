from flask import Flask, request
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def getIndex():
    return "Hello World!"

@app.route('/api/reserve', methods=['POST'])
def getData():
    data = request.get_json()

    if data is None:
        return "Bad Request: JSON data not provided", 400

    name = data.get("name")
    surname = data.get("surname")

    if name is None or surname is None:
        return "Bad Request: Name and surname are required", 400
    print(name)
    print(surname)

    jsonObject = {
        "name": name,
        "surname": surname
        # Add other fields as needed
    }
    

    with open('data.json','r') as file:
        data = json.load(file)
        data.append(jsonObject)
            

    with open('data.json', 'w') as db:
        json.dump(data, db, indent=4)
        

    return "Data saved successfully"

if __name__ == '__main__':
    app.run(debug=True)
