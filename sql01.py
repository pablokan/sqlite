import sqlite3

conn = sqlite3.connect('personas.db')
cursor = conn.cursor()
cursor.execute(
    "INSERT INTO personas (nombre, edad) VALUES (?, ?)", 
    ('tercero', 2)
)            
conn.commit()
conn.close()
