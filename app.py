from flask import Flask, render_template, request
import pymongo


app = Flask(__name__)
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.pro_programmer
collection = db.Blog

# Routes
@app.route("/")
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def onsearch():
    if request.method == 'POST':
        find = db.Blog.find(
            {"title": {"$regex": request.form.get('searchtext')}})
        if find:
            return render_template('search.html', noblog=False, blog=find)
        else:
            return render_template('search.html', noblog=True)

    else:
        print('no')


@app.route("/blog/<string:slug>",methods=['GET'])
def blog(slug):
    print(request.method)
    if request.method == 'GET':
        query = db.Blog.find({"slug":slug})
        if query:
            return render_template('slug.html', data = query, noSlug = False)
        else:
            return render_template('slug.html', noSlug = True)
    else:
        print('Invaild Request')
        
@app.route("/blog",methods=['GET'])
def allblog():
    print(request.method)
    if request.method == 'GET':
       findallblog = db.Blog.find().limit(4)
       if findallblog:
           return render_template('search.html', noblog=False, blog=findallblog)
       else:
           return render_template('search.html', noblog=True)
            

    else:
        print('Invaild Request')
# Runing app
if __name__ == '__main__':
    app.run(debug=True)
