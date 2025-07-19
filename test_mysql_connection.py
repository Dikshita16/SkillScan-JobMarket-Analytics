import pymysql

# Connect to MySQL
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Hatte@1604',  # ← Replace this with your actual MySQL password
    database='skillscan'
)

cursor = connection.cursor()

cursor.execute("SHOW TABLES;")
for row in cursor.fetchall():
    print(row)

connection.close()
