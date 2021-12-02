from flask import Flask, render_template, request
import pymongo
app = Flask(__name__)

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.pro_programmer
collection = db.Blog
# collection.insert_one({
#     'name':'Mohit',
#     'Age':12
# })


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def onsearch():
    # print(request.form.get('username'))
    # print(request.method)
    # print(request.form.get('searchtext'))
    if request.method == 'POST':
        find = db.Blog.find({"title": request.form.get('searchtext')})
        if find:
            return render_template('search.html', noblog = False, blog = find)
        else:
            return render_template('search.html', noblog = True)

    else:
        print('no')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
