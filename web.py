from flask import Flask, render_template, request, redirect, session, flash
import os
import pymongo
from pymongo import MongoClient

from scraper import q, price

app = Flask(__name__)
#Creates a key for the session
app.secret_key = os.urandom(24)
#This connects to the database online
client = MongoClient("mongodb://ames4life:cs314@webscrapy-shard-00-00-gre6l.mongodb.net:27017,webscrapy-shard-00-01-gre6l.mongodb.net:27017,webscrapy-shard-00-02-gre6l.mongodb.net:27017/test?ssl=true&replicaSet=WebScrapy-shard-0&authSource=admin&retryWrites=true")
db = client['mydb']
collection = db['accounts']

#Template store the html files

#This is the login page.
@app.route('/', methods=['POST','GET'])
def login():
    if(request.method == 'POST'):

        if(request.form['username'] is not None and request.form['password'] is not None):
            # Time to check credentials
            doc = db.accounts.find_one({"username" : request.form['username']}, {"password" : request.form['password']} )
            if(doc is not None):
                #print("Working!")
                session['username'] = request.form['username']
                return redirect("/home", code=200)
            #else:
             #   print("Not Working")



    else:
        pass
    #index.html is actually login html file
    return render_template("index.html")


@app.route('/signup', methods=['POST','GET'])
def signup():
    #request.method == 'POST' means it checks when the submit button is clicked and processes the data.
    if(request.method == 'POST'):
        if(request.form['submit'] == 'Enter'):
            account = {
                "firstname" : request.form['firstname'],
                "lastname" : request.form['lastname'],
                "username" : request.form['username'],
                "password" : request.form['password'],
                "email" : request.form['email']
            }

            accounts = db.accounts
            #Inserts a document to a collection.
            account_id = accounts.insert_one(account).inserted_id
            # Success so redirect to login page.
            return redirect("/", code=200)
    else:
        pass

    return render_template("signup.html")

@app.route('/home', methods=['POST','GET'])
def home():
    return render_template("home.html")


@app.route('/quotes/<int:id>', methods=['POST','GET'])
def quotes(id):
    # p  = q.get_page('http://quotes.toscrape.com/')
    htmlDoc = open('./Lib/site-packages/templates/quotes.html', 'r+')
    t = q.update('http://quotes.toscrape.com/page/' + str(id) + '/', htmlDoc)

    return render_template('quotesout.html')

@app.route('/prices/<int:id>', methods=['POST','GET'])
def prices(id):
    # p  = q.get_page('http://quotes.toscrape.com/')
    htmlDoc = open('./Lib/site-packages/templates/price.html', 'r+')

    t = price.update('https://www.amazon.com/s?k=computer/' + str(id) + '/', htmlDoc)
    return render_template('priceout.html')

#Testing what user is in session.
@app.route('/getSession')
def getSession():
    if 'username' in session:
        return session['username']

@app.route('/logout')
def logout():
    session.pop('user',None)
    flash('You were logged out')
    return redirect("/", code=200)

app.run(debug=True)