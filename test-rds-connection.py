import os

import pymysql 
from pymysql import err
from dotenv import load_dotenv

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
    
def main():
    load_dotenv(verbose=True)
    host = os.getenv("RDS_HOST")
    username = os.getenv("RDS_USERNAME")
    database = os.getenv("RDS_DATABASE")
    password = os.getenv("RDS_USERPASSWORD")
    port = 3306

    cursor = connect_rds(host, port, username, password, database)

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
        VALUES ('혜정', 'seathat33@gmail.com', '2023-10-29');
    '''
    cursor.execute(insert_user_sql)
    
    


    select_user_query = "SELECT * FROM user"
    cursor.execute(select_user_query)

    users = cursor.fetchall()
    for user in users:
        print(user)

    
if __name__ == "__main__":
    main()
