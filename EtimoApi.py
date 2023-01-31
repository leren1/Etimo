#
# Lucas Eren
# EtimoApi.py
# 

from flask import Flask, jsonify, request
import sqlite3
from waitress import serve

# The function deletes the user from the database
def deleteUser(userEmail):
    message = {}
    try:
        connection = sqlite3.connect('etimoDatabase.db')
        cur = connection.cursor()
        cur.execute("DELETE from etimo WHERE email = ?", (userEmail,))
        connection.commit()
        message["status"] = "User deleted successfully"
    except:
        connection.rollback()
        message["status"] = "Cannot delete user"
    finally:
        cur.close()
    return message

# The function shows all users in the database
def showAllusers():
    connection = sqlite3.connect('etimoDatabase.db')
    cur = connection.cursor()
    rows = cur.execute("SELECT * FROM etimo").fetchall()
    users = []
    for r in rows: 
        users.append(r)
    connection.close()
    return users

# The function adds a user to the database. 
# In the first few lines there is input validation so that the input for email, firstname and lastname is not an empty string 
def addUser(newUser):
    message = {}
    
    if(newUser['email'].strip() == ""):
        message["status"] = "You cant have an empty email"
        return message
    elif(newUser['firstname'].strip() == ""):
        message["status"] = "You cant have an empty firstname"
        return message
    elif(newUser['lastname'].strip() == ""):
        message["status"] = "You cant have an empty lastname"
        return message

    try:
        connection = sqlite3.connect('etimoDatabase.db')
        cur = connection.cursor()
        cur.execute("INSERT INTO etimo (email, firstname, lastname) VALUES (?, ?, ?)", (newUser['email'],   
                    newUser['firstname'], newUser['lastname']))
        connection.commit()
        message["status"] = "User added successfully"
    except sqlite3.IntegrityError as e:
        message["status"] = "Email is already taken"
    finally:
        connection.close()
    return message


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Lets go Etimo :)'

@app.route('/addUser', methods=['POST'])
def add():
    newUser = request.get_json()
    return jsonify(addUser(newUser))

@app.route('/deleteUser/<userEmail>', methods=['DELETE'])
def delete(userEmail):
    return jsonify(deleteUser(userEmail))

@app.route('/showUsers', methods=['GET'])
def showAll():
    return jsonify(showAllusers())


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
    app.run()
