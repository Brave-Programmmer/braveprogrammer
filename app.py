from flask import Flask, render_template
import pymongo
app = Flask(__name__)

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.pro_programmer
collection = db.user

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')
if __name__ == '__main__':
    app.run(debug=True)
