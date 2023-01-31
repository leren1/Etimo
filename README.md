# Etimo assignment
### Before starting, you need to install: 
* pip install Flask
* pip install db-sqlite3
* pip install waitress

### To start the program 
1. Run the EtimoDb.py file to create the database. 
2. Run EtimoApi.py to start server and enable the different REST API calls.
3. In test.py it exist some test cases which you can run when step 2 is completed. 

### To test the code with curl:
### Add a user:
* curl -H "Content-Type: application/json" -X POST -d '{"email": "something@gmail.com", "firstname": "Something", "lastname": "Something"}' http://localhost:8080/addUser

#### Delete a user: 
* curl -X DELETE http://127.0.0.1:8080/deleteUser/<The email account you want to delete>

#### Show all users:
* curl -v http://127.0.0.1:8080/showUsers

