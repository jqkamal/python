import sqlite3
conn =sqlite3.connect(('ss.db'))
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS SELA")
sql='''CREATE TABLE SELA(na CHAR(20),num int,ads CHAR(1),br char(20),
nam char(20),ra char,ro char,amo int,qty int)'''
cursor.execute(sql)
print("Table created successfully....")
conn.commit()
conn.close()
