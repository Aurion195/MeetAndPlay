from flask import Flask, make_response, jsonify, request
import os
import dataset
from flask_cors import CORS
app = Flask(__name__)
db = dataset.connect('sqlite:///../database/database.sqlite')
cors = CORS(app)

eventsTable = db['events']
usersTable = db['Users']

def fetch_db(event_id):  # Each book scnerio
    return eventsTable.find_one(id=event_id)


def fetch_db_all():
    events = []
    for event in eventsTable:
        events.append(event)
    return events


def fetch_User_db(user_id):  # Each book scnerio
    return usersTable.find_one(id=user_id)


def fetch_User_db_all():
    users = []
    for user in usersTable:
        users.append(user)
    return users


@app.route('/getallevent', methods=['GET'])
def api_events():
    if request.method == "GET":
        return make_response(jsonify(fetch_db_all()), 200)

@app.route('/geteventbyid/<event_id>', methods=['GET'])
def api_each_event(event_id):
    print(event_id)
    if request.method == "GET":
        event_obj = fetch_db(event_id)
        if event_obj:
            return make_response(jsonify(event_obj), 200)
        else:
            return make_response(jsonify(event_obj), 404)

@app.route('/getallusers', methods=['GET'])
def api_users():
    if request.method == "GET":
        return make_response(jsonify(fetch_User_db_all()), 200)

@app.route('/getuserbyid/<user_id>', methods=['GET'])
def api_each_user(user_id):
    print(user_id)
    if request.method == "GET":
        user_obj = fetch_User_db(user_id)
        if user_obj:
            return make_response(jsonify(user_obj), 200)
        else:
            return make_response(jsonify(user_obj), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))