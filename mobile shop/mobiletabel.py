
import sqlite3
conn =sqlite3.connect(('ss.db'))
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS ADDMOBILE")
sql='''CREATE TABLE ADDMOBILE(br char(10),nam CHAR(20),col char(10),ra int,ro int,cam char(20),
pro char(20),bat char(20),amo int,qty int)'''
cursor.execute(sql)
print("Table created successfully....")
conn.commit()
conn.close()
