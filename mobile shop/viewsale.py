import sqlite3
conn = sqlite3.connect('ss.db')
cursor = conn.cursor()
cursor.execute('''SELECT * from sale''')
result=cursor.fetchone()
print(result)
conn.commit()
conn.close()
