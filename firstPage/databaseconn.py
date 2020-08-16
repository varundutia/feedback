import mysql.connector as mysql
db = mysql.connect(
    host='localhost',
    user='root',
    passwd='Varun@12061999'
)
print(db)
cursor = db.cursor()
cursor.execute("SHOW DATABASES")
dbs = cursor.fetchall()
for d in dbs:
    print(d)