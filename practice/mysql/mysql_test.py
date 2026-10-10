import os
import pymysql
from getpass import getpass

password = os.environ.get("MYSQL_PASSWORD") or getpass("MySQL password: ")

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password=password,
    database="study_db",
    charset="utf8mb4"
)

print("MySQL连接成功！")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

row = cursor.fetchone()
print(row)
conn.close()