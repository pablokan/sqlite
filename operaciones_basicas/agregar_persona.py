cursor.execute(
    "INSERT INTO personas (nombre, edad) VALUES (?, ?)", 
    ('tercero', 2)
)            
conn.commit()