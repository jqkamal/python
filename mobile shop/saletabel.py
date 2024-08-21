
import sqlite3
conn =sqlite3.connect(('ss.db'))
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS SALE")
sql='''CREATE TABLE SALE(na char(10),num CHAR(20),ads char(20),br char,bna char(20),ra char(20),ro char,amo int,qty int)'''
cursor.execute(sql)
print("Table created successfully....")
conn.commit()
conn.close()
