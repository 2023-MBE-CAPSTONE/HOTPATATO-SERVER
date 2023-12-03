import os

import pymysql 
from pymysql import err
from dotenv import load_dotenv
import datetime

from api.user import user_route


from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
app.register_blueprint(user_route)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/lastnews')
def lastnews():
   return render_template('last_news.html')


if __name__ == '__main__':  
   app.run(host = '0.0.0.0',port=5001,debug=True)