import pymysql

try:
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        database='prac2'
    )

    query = 'SELECT * FROM employee;'
    print(f"Executing query: {query}")
    
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()
    

    cur.close()
    conn.close()

except pymysql.MySQLError as err:
    print(f"Error: {err}")
except Exception as e:
    print(f"Exception: {e}")