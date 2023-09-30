from flask import Flask, request
from src import UserRepo

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/insert", methods=["POST"] )
def insert():
    users_repo = UserRepo()
    body = request.json
    users_repo.insert_user(body["name"])
    return 'OK'