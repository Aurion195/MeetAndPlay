#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, make_response, jsonify, request,Response
import os
import json
import dataset
from flask_cors import CORS,cross_origin
from flask.helpers import flash
from passlib.hash import sha256_crypt 
app = Flask(__name__)
db = dataset.connect('sqlite:///../database/database.sqlite')
cors = CORS(app)

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
        usersTable.insert(dict(
            username=newuser['username'],
            prenom=newuser['firstname'],
            nom=newuser['lastname'],
            age=newuser['age'],
            password=newuser['secure_password'],
            adresse=newuser['adresse'],
            tel=newuser['tel'],
            mail=newuser['mail'],
            avatar = " ",
            jeu_favoris=" ",
            activité_recente=" ",
            nombre_victoire="0",
            note=" ",
            niveau="0",
            ))
        return True


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        password = request.form.get('password')
        newuser={
            "username" : request.form.get('username'),
            "firstname" : request.form.get('prenom'),
            "lastname" : request.form.get('nom'),
            "age" : request.form.get('age'),
            "secure_password" : sha256_crypt.encrypt(str(password)),
            "adresse" : request.form.get('adresse'),
            "tel" : request.form.get('tel'),
            "mail" : request.form.get('mail'),
        }
        if add_user(newuser) == True:
               
        
                return build_actual_response(jsonify("status : OK"))
        else:
            return  make_response(jsonify("status : KO"), 404)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        usernamedata = usersTable.find_one(usename=username)

    if usernamedata is None:
        return make_response(jsonify("status : KO , error : User no found"), 404)
    else:
        for password in usernamedata["password"]:
            if sha256_crypt.verify(password, usernamedata["password"]):
                session['log'] = True
                return make_response(jsonify("status : OK, message : Logged in successfully"), 200)
            else:
               return make_response(jsonify("status : KO, message : Wrong password"), 400)

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
