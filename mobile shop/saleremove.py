import sqlite3
conn=sqlite3.connect('ss.db')
cursor=conn.cursor()
br=input('enter the brand')
na=input('enter the name')
ra=input('enter the ram')
ro=input('enter the rom ')
qty=input('enter the quantity')
sql=cursor.execute("UPDATE  FROM addmobile where br=? and nam=? and ra=? and ro=? and qty=?",(br,na,ra,ro,qty))
conn.commit()
print("records sale.....")
conn.close()