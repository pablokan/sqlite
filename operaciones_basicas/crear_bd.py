import sqlite3

conn = sqlite3.connect('gente.db') # hace la conexión
cursor = conn.cursor() # crea la estructura de control de los datos
cursor.execute( # ejecuta la instrucción SQL de creación de la tabla
        "CREATE TABLE IF NOT EXISTS personas \
        (id INTEGER PRIMARY KEY, \
        nombre TEXT NOT NULL, \
        edad INTEGER NOT NULL)"
)
conn.commit()
