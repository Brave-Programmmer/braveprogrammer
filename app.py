from flask import Flask, render_template, request
import pymongo
app = Flask(__name__)

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.pro_programmer
collection = db.user
# collection.insert_one({
#     'name':'Mohit',
#     'Age':12
# })


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/api/v1/login', methods=['GET', 'POST'])
def onlogin():
    return
        # print(request)
        # if request.method == 'POST':
        #     find = collection.find_one(
        #         {'username': request.username, 'password': request.password})

    
@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
