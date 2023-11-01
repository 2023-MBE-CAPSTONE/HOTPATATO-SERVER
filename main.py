import os

import pymysql 
from pymysql import err
from dotenv import load_dotenv
import datetime


def connect_rds(host, port, username, password, database):
    try:
        conn = pymysql.connect(
            host=host, 
            user = username, 
            passwd = password, 
            db = database, 
            port = port, 
            use_unicode = True, 
            charset = 'utf8'
        )
        cursor = conn.cursor()
    except err.OperationalError as e:
        print(f"User Database Connection Error: {e}")
        cursor = None
    return cursor


from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/test", methods=["POST"])
def info_post():
    email_receive = request.form['email_give']
    name_receive = request.form['name_give']
    
    load_dotenv(verbose=True)
    host = os.getenv("RDS_HOST")
    username = os.getenv("RDS_USERNAME")
    database = os.getenv("RDS_DATABASE")
    password = os.getenv("RDS_USERPASSWORD")
    port = 3306

    cursor = connect_rds(host, port, username, password, database)
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    """
    creat_table_sql =  '''CREATE TABLE user (
		user_id int(10) AUTO_INCREMENT PRIMARY KEY,
		user_name varchar(255) NOT NULL,
		email_address varchar(255) NOT NULL,
		signup_date DATE NOT NULL
    )'''
    cursor.execute(creat_table_sql)
    """
    
    show_tables_query = "SHOW TABLES"
    cursor.execute(show_tables_query)
    tables = cursor.fetchall()
    for table in tables:
        print(f"{table} table in hotpotato rds")
    
    
    insert_user_sql = '''
        INSERT INTO user (user_name, email_address, signup_date)
        VALUES (%s, %s, %s);
    '''
    cursor.execute(insert_user_sql, (name_receive, email_receive, current_date))
    
    


    select_user_query = "SELECT * FROM user"
    cursor.execute(select_user_query)

    users = cursor.fetchall()
    for user in users:
        print(user)
    return jsonify({'msg': '구독 완료!'})


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)