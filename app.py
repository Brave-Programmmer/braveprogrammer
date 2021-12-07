from flask import Flask, render_template, request, Markup

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


@app.route("/blog/<string:slug>", methods=['GET'])
def blog(slug):
    print(request.method)
    if request.method == 'GET':
        query = db.Blog.find({"slug": slug})
        if query:
            return render_template('slug.html', data=query, noSlug=False, Markup=Markup)

        else:
            return render_template('slug.html', noSlug=True)
    else:
        print('Invaild Request')


@app.route("/blog", methods=['GET'])
def allblog():
    if request.method == 'GET':
        req1 = request.args.get('from')
        req2 = request.args.get('to')
        if req1 and req2:
            findallblog = db.Blog.find().skip(int(req1)).limit(int(req2))
            numblog = db.Blog.count_documents({})
            if findallblog:
                next_url = int(req1) + 4
                pre_url = int(req2) + 4
                next_url1 = int(req1) - 4
                pre_url1 = int(req2) - 4
                return render_template('search.html', noblog=False, 
                numblog = numblog
                blog=findallblog, next_url=next_url, pre_url = pre_url, next_url1=next_url1, pre_url1 = pre_url1)
            else:
                return render_template('search.html', noblog=True)
        else:
            return print('404')

    else:
        return print('Invaild Request')


# Runing app
if __name__ == '__main__':
    app.run(debug=True)
