#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, make_response, jsonify, request,Response
import os
import json
import dataset
from flask_cors import CORS,cross_origin
from flask.helpers import flash
from passlib.hash import sha256_crypt
import sqlite3

app = Flask(__name__)
cors = CORS(app)#, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

db = dataset.connect('sqlite:///../database/database.sqlite')

eventsTable = db['events']
usersTable = db['Users']


def build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
    
def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def fetch_db(event_id):  # Each book scnerio
    return eventsTable.find_one(id=event_id)


def fetch_db_all():
    events = []
    for event in eventsTable:
        events.append(event)
    return events


def fetch_User_db(user_id):  # Each book scnerio
    return usersTable.find_one(id=user_id)

def deleteUser_db(user_id):  # Each book scnerio
    if usersTable.delete(id=user_id):
            return True
    else:
            return False

def fetch_User_db_all():
    users = []
    for user in usersTable:
        users.append(user)
    return users


def add_user(newuser):
    if usersTable.find_one(username=newuser):
        return False
    else:
         
        result = db.execute('INSERT INTO Users (prenom ,nom,username,password,tel,mail,avatar,adresse,age ,jeu_favoris,activité_recente,nombre_victoire ,note ,niveau) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
                    (
                    newuser['username'],
                    newuser['firstname'],
                    newuser['lastname'],
                    newuser['age'],
                    newuser['password'],
                    newuser['adresse'],
                    newuser['tel'],
                    newuser['mail'],
                    newuser["avatar "],
                    newuser["jeu_favoris"],
                    newuser["activité_recente"],
                    newuser["nombre_victoire"],
                    newuser["note"],
                    newuser["niveau"]
                    )
                )
        return result
    
        

@app.route('/register', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def register():
    if request.method == 'POST':
        newuser=request.get_json()
        tmp = usersTable.insert(dict(
            username=newuser['username'],
            prenom=newuser['prenom'],
            nom=newuser['nom'],
            age=newuser['age'],
            password=newuser['password'],
            adresse=newuser['adresse'],
            tel=newuser['tel'],
            mail=newuser['mail'],
            avatar = " ",
            jeu_favoris=newuser['jeu_favoris'],
            activité_recente=" ",
            nombre_victoire=0,
            note=0,
            niveau=0,
            ))
        
        return jsonify({ 'Status': "OK" }), 200
    else:
        return jsonify({"status" : "KO"}), 400


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.get_json()
        username = user['username']
        password = user['password']
        usernamedata = None
        con = sqlite3.connect('../database/database.sqlite')
        cursor = con.cursor()
        userData =  cursor.execute('SELECT password FROM Users WHERE username = ? ', [username])
        result = cursor.fetchone()
        passwordData = result[0]
        if userData is None:
            return jsonify({"status": "KO" , "error" : "User no found"}), 405
        else:
                if (password == passwordData):
                    return jsonify({"status" : "OK", "message" : "Logged in successfully"}), 200
                else:
                    return jsonify({"status" : "KO", "message" : "Wrong password"}), 204
    else:
        return jsonify({"status":"KO", "message":"error"}),405

@app.route('/getallevent', methods=['GET'])
def api_events():
    if request.method == 'GET':
        return make_response(jsonify(fetch_db_all()), 200)



@app.route('/deleteUser/<user_id>', methods=['GET'])
def deleteUser(user_id):
    if request.method == 'GET':
        if deleteUser_db(user_id):
            return make_response(jsonify("status : OK, message : Deleted successful"), 200)
        else:
            return make_response(jsonify("status : KO, message : Deleted not successful"), 400)




@app.route('/geteventbyid/<event_id>', methods=['GET'])
def api_each_event(event_id):
    if request.method == 'GET':
        event_obj = fetch_db(event_id)
        if event_obj:
            return make_response(jsonify(event_obj), 200)
        else:
            return make_response(jsonify(event_obj), 404)


@app.route('/getallusers', methods=['GET'])
def api_users():
    if request.method == 'GET':
        return make_response(jsonify(fetch_User_db_all()), 200)


@app.route('/getuserbyid/<user_id>', methods=['GET'])
def api_each_user(user_id):
    if request.method == 'GET':
        user_obj = fetch_User_db(user_id)
        if user_obj:
            return make_response(jsonify(user_obj), 200)
        else:
            return make_response(jsonify(user_obj), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
