#
# Lucas Eren
# test.py
# 

from EtimoApi import app, addUser, showAllusers, deleteUser
from waitress import serve
import requests
import unittest

class test(unittest.TestCase):

    # Check for respons 200 
    def testStatusCode(self):
        r = requests.get("http://127.0.0.1:8080/")
        self.assertEqual(r.status_code, 200)

    # Add user to database
    def testAddUser(self):
        newUser = {'email': 'Joel@example.com', 'firstname': 'Joel', 'lastname': 'Joelsson'}
        requests.post("http://127.0.0.1:8080/addUser", json=newUser)
        r = requests.get("http://127.0.0.1:8080/showUsers")       
        dataBase = r.json()
        self.assertEqual(dataBase[-1][0], "Joel@example.com")
        self.assertEqual(dataBase[-1][1], "Joel")
        self.assertEqual(dataBase[-1][2], "Joelsson")

    # Throws status code 500 due to creating a new user with an already existing email.
    def testAddWithSameEmail(self):
        newUser = {'email': 'Joel@example.com', 'firstname': 'Joel', 'lastname': 'Joelsson'}
        r = requests.post("http://127.0.0.1:8080/addUser", json=newUser)
        self.assertEqual(r.text, '{"status":"Email is already taken"}\n')

    # Delete user from database
    def testDeleteUser(self):
        userEmail = "Joel@example.com"
        requests.delete("http://127.0.0.1:8080/deleteUser/" + userEmail)
        r = requests.get("http://127.0.0.1:8080/showUsers")
        dataBase = r.json()
        self.assertNotEqual(dataBase[-1][0], "Joel@example.com")

if __name__ == '__main__':
    unittest.main()