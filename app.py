from flask import Flask, render_template, request, Markup
import math
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.pro_programmer
collection = db.Blog
loggedin = False
# Routes


@app.route("/")
def home():
    find = db.Blog.find({}).limit(4)
    return render_template('index.html', allblog=find)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            auth = db.user.find_one(
                {'username': username, 'password': password})
            if auth:
                find = db.Blog.find({}).limit(6)
                return render_template('admin.html', loggedin=True, username=username, password=password, allblog=find)
            else:
                return render_template('admin.html', loggedin='Invalid')

    elif request.method == 'GET':
        # print(loggedin)
        return render_template('admin.html', loggedin=False)
    else:
        return print('Errror')


@app.route('/search', methods=['GET', 'POST'])
def onsearch():
    if request.method == 'POST':
        pageno = int(request.args.get('page'))  # Current Page eg 2
        noblogs = db.Blog.count_documents(
            {"contain": {"$regex": request.form.get('searchtext')}})  # Total no of blogs 16
        nopages = math.ceil(noblogs/4)  # no of pages can be made 4
        print(nopages)
        # first page
        if pageno == 1:
            findallblog = db.Blog.find({"contain": {"$regex": request.form.get(
                'searchtext')}}).skip((pageno * pageno) - 1).limit(4)
            pre_url = "no"
            next_url = f'/blog?page={pageno + 1}'
            # print(next_url)
            return render_template(
                'search.html',
                allblog=findallblog,
                Markup=Markup,
                pageno=pageno,
                pre_url=pre_url,
                next_url=next_url
            )
        elif pageno == nopages:
            findallblog = db.Blog.find({}).skip((pageno * pageno) - 1).limit(4)
            pre_url = f'/blog?page={pageno - 1}'
            next_url = "no"
            # print(next_url)
            return render_template(
                'search.html',
                allblog=findallblog,
                Markup=Markup,
                pageno=pageno,
                pre_url=pre_url,
                next_url=next_url
            )
        else:
            findallblog = db.Blog.find({}).skip((pageno * pageno) - 1).limit(4)
            pre_url = f'/blog?page={pageno - 1}'
            next_url = f'/blog?page={pageno + 1}'
            # print(next_url)
            return render_template(
                'search.html',
                allblog=findallblog,
                Markup=Markup,
                pageno=pageno,
                pre_url=pre_url,
                next_url=next_url
            )

    # if request.method == 'POST':
    #     find = db.Blog.find({"contain": {"$regex": request.form.get('searchtext')}})
    #     if find:
    #         return render_template('search.html', noblog=False, allblog=find)
    #     else:
    #         return render_template('search.html', noblog=True)

    # else:
    #     print('no')


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
        pageno = int(request.args.get('page'))  # Current Page eg 2
        noblogs = db.Blog.count_documents({})  # Total no of blogs 16
        nopages = math.ceil(noblogs/4)  # no of pages can be made 4
        print(nopages)
        # first page
        if pageno == 1:
            findallblog = db.Blog.find({}).skip((pageno * pageno) - 1).limit(4)
            pre_url = "no"
            next_url = f'/blog?page={pageno + 1}'
            # print(next_url)
            return render_template(
                'search.html',
                allblog=findallblog,
                Markup=Markup,
                pageno=pageno,
                pre_url=pre_url,
                next_url=next_url
            )
        elif pageno == nopages:
            findallblog = db.Blog.find({}).skip((pageno * pageno) - 1).limit(4)
            pre_url = f'/blog?page={pageno - 1}'
            next_url = "no"
            # print(next_url)
            return render_template(
                'search.html',
                allblog=findallblog,
                Markup=Markup,
                pageno=pageno,
                pre_url=pre_url,
                next_url=next_url
            )
        else:
            findallblog = db.Blog.find({}).skip((pageno * pageno) - 1).limit(4)
            pre_url = f'/blog?page={pageno - 1}'
            next_url = f'/blog?page={pageno + 1}'
            # print(next_url)
            return render_template(
                'search.html',
                allblog=findallblog,
                Markup=Markup,
                pageno=pageno,
                pre_url=pre_url,
                next_url=next_url
            )
        # Last Page
        # elif pageno == nopages:
        #     findallblog = db.Blog.find({}).skip((pageno * pageno) - 1).limit(4)
        #     return render_template('search.html', allblog=findallblog, Markup=Markup, pageno=pageno)
        # findallblog = db.Blog.find({}).skip((pageno * pageno)).limit(4)
        # if pageno < nopages or pageno == nopages:
        #     return render_template('search.html', allblog=findallblog, Markup=Markup)
        # else:
        #     return print('no page')


# Runing app
if __name__ == '__main__':
    app.run(debug=True)
