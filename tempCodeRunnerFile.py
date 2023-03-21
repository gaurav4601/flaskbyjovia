ith cnx.cursor() as cur:
    cur.execute("""CREATE TABLE mytable (
                name VARCHAR(255) NOT NULL,
                age INT NOT NULL,
                mobile_no VARCHAR(20) NOT NULL
                );"""
                )