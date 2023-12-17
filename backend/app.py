from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

def getTime(time, DATA):
    time_str1 = time
    time_str2 = str(int(time.split(':')[0]) + 2)+ ':' + time.split(':')[1]
    # print(time_str1)
    # print(time_str2)
    # print(DATA)
    # print('------------')

    # Today's date as a placeholder (you can use any date)
    today_date = datetime.now().date()

    # Parse the time strings into datetime objects
    time1 = datetime.strptime(f"{today_date} {time_str1}", "%Y-%m-%d %H:%M")
    time2 = datetime.strptime(f"{today_date} {time_str2}", "%Y-%m-%d %H:%M")
    dataTime = datetime.strptime(f"{today_date} {DATA}", "%Y-%m-%d %H:%M")
    # print(time1)
    # print(time2)
    # print(dataTime)

    # Compare the two datetime objects
    if time1 > dataTime or dataTime > time2:
        return True
    return False


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
    numTables = data.get("numTables")
    numPeople = data.get("numPeople")   #
    time = data.get("time")             #
    date = data.get("date")
    tel = data.get("tel")
    email = data.get("email")

    if name is None or surname is None:
        return "Bad Request: Name and surname are required", 400





    # with open(r'D:\User\Desktop\ITakaProba\ITakaSiBeshe\rezervacii.json', 'r') as file:
    #     DATA = json.load(file)

    # if getTime(time, DATA="00:01"):
    #     print('Taman Time')
    # else:
    #     return jsonify(400) # Nemojt to vreme




    jsonObject = {
        "name": name,
        "surname": surname,
        "numPeople": numPeople,
        "numTables": numTables,
        "time": time,
        "date": date,
        "tel": tel,
        "email": email

    }


    with open(r'D:\User\Desktop\ITakaProba\ITakaSiBeshe\rezervacii.json', 'r') as file:
        data = json.load(file)
        data.append(jsonObject)

    # DATA.append(jsonObject)
            

    with open(r'D:\User\Desktop\ITakaProba\ITakaSiBeshe\rezervacii.json', 'w') as db:
        json.dump(data, db, indent=4)
        

    return jsonify(200)



if __name__ == '__main__':
    app.run(debug=True)