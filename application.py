import mysql.connector

cnx = mysql.connector.connect(
    host='ap-south.connect.psdb.cloud',
    user='793vlt7yzqickihdkp1y',
    password='pscale_pw_orSDQ6HupAlG65x9oRen1nrPAwGzdFFAX0upGqo3C8U',
    database='joviancarrer'
)

# with cnx.cursor() as cur:
#     cur.execute("""CREATE TABLE userapplication (
#                 name VARCHAR(255) NOT NULL,
#                 age INT NOT NULL,
#                 mobile_no VARCHAR(20) NOT NULL
#                 );"""
#                 )
# with cnx.cursor() as cur:
#         query = """INSERT INTO userapplication (name, age, mobile_no)
#         VALUES ('John Doe', 30, '123-456-7890'),
#                 ('Jane Smith', 25, '555-555-5555'),
#                 ('Bob Johnson', 45, '555-123-4567');
#                 """
#         cur.execute(query)



with cnx.cursor() as cur:
    cur.execute("SELECT * FROM userapplication")
    print(cur.fetchall())





def apply_job(name,age,mobile):
    with cnx.cursor() as cur:
        query = """INSERT INTO userapplication(name, age, mobile_no)
                VALUES ('GAURAV', 26, '7020558915');"""
        cur.execute(query)
