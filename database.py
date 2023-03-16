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

import mysql.connector
#from cred import cred




cnx = mysql.connector.connect(
    host=cred['host'],
    user=cred['user'],
    password=cred['password'],
    database=cred['database']
)



def get_jobsdata():
    cursor = cnx.cursor()
    with cursor as cur:
        print('connection successful')
        cur.execute("SELECT * FROM jobs");
        # get column names
        columns = [col[0] for col in cur.description]
        results = cursor.fetchall()
        result_dict = []
        for row in results:
            result_dict.append(dict(zip(columns,row)))
        #printing the results dict
        return result_dict
    
    
    