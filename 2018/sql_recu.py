import sqlite3

con = sqlite3.connect("baseci")
cur = con.cursor()

cur.execute("SELECT Nombre FROM Gente ORDER BY Nombre")

rows = cur.fetchall()
for row in rows:
    print row[0]

con.close()

