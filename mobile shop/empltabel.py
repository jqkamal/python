import sqlite3
conn =sqlite3.connect(('ss.db'))
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql='''CREATE TABLE EMPLOYEE(ids int,na CHAR(20),ag int,gen CHAR(1),pas char(20),
em char(20),ad char(20),con int,sly int)'''
cursor.execute(sql)
print("Table created successfully....")
conn.commit()
conn.close()
