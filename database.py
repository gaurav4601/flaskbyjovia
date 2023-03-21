# from sqlalchemy import create_engine, Column, Integer, String


# # create a database engine
# engine = create_engine('mysql+mysqlconnector://o0rznxamktbumyz3pug9:pscale_pw_uETfoSZq8e3TaDTljBUUThkxxox6VZlln3Bc0iduPrZ@ap-south.connect.psdb.cloud:3306/joviancarrer')


# with engine.connect() as conn:
#     result = conn.execute("SELECT * FROM jobs;")
#     print('===========')
#     print(type(result.all()))
#     print('===========')
#     print(result.all())
# # test the connection
# try:
#     connection = engine.connect()
#     print('Connection successful!')
# except:
#     print('Connection failed!')
# finally:
#     connection.close()

import os
import mysql.connector
from cred import cred




cnx = mysql.connector.connect(
    host=cred['host'],
    user=cred['user'],
    password=cred['password'],
    database=cred['database']
)

# cnx = mysql.connector.connect(
#     host=os.environ['host'],
#     user=os.environ['user'],
#     password=os.environ['password'],
#     database=os.environ['database']
# )



def get_jobsdata(id=None):
    if id:
        with cnx.cursor() as cur:
            query = "SELECT * FROM jobs WHERE id =" + str(id) + ';'
            cur.execute(query)
            # get column names
            columns = [col[0] for col in cur.description]
            results = cur.fetchall()
            result_dict = []
            for row in results:
                result_dict.append(dict(zip(columns,row)))
            #printing the results dict
            return result_dict
    else:
        with cnx.cursor() as cur:
            cur.execute("SELECT * FROM jobs;")
            # get column names
            columns = [col[0] for col in cur.description]
            results = cur.fetchall()
            result_dict = []
            for row in results:
                result_dict.append(dict(zip(columns,row)))
            #printing the results dict
            return result_dict
        
    
    