import sqlite3
from inputs import *

class CrudSQLite:
    def __init__(self, db_name: str, fields: list) -> None:
        self.conn = sqlite3.connect(db_name+'.db')
        self.cursor = self.conn.cursor()
        self.table_name = db_name
        self.fields = [field.split()[0] for field in fields]
        full_fields = ', '.join(fields)
        query = f"CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER PRIMARY KEY, {full_fields})"
        self.cursor.execute(query)
        self.conn.commit()
        
    def add(self, *args):
        field_names = ', '.join(self.fields)
        fields_list = [f"'{field}'" if type(field)==str else str(field) for field in args]
        field_values = ", ".join(fields_list)
        query = f"INSERT INTO {self.table_name} ({field_names}) VALUES ({field_values})"
        #print(query)
        self.cursor.execute(query)
        self.conn.commit()
        
    #def mod(self, id, *args):
    #    query = f"UPDATE {self.table_name} SET "
    #    self.cursor.execute(query)

    def listar(self):
        print('Listado')
        def kprint(lista_diccionarios):
            for diccionario in lista_diccionarios:
                linea = " - ".join(f"{clave}: {valor}" for clave, valor in diccionario.items())
                print(linea)

        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        todo = self.cursor.fetchall()
        campos = self.fields
        lista_completa = [{k: v for k, v in zip(campos, fila)} for fila in todo]
        kprint(lista_completa)

    def eliminar(self, id):
        self.cursor.execute(f"DELETE FROM personas WHERE id = {id}")
        self.conn.commit()

    def cerrar_db(self):
        self.conn.close()

if __name__ == '__main__':
    articles = ['item TEXT', 'qty INTEGER', 'prize REAL']
    b = CrudSQLite('negocio', articles)
    op = inputChoiceMenu('Altas/Bajas/Modificaciones/Listado')
    print(op)



    #b.add('mesa', 10, 2.3)
    #b.add('silla', 20, 222.3)
    #b.listar()
    #b.mod(2, 'sillita', 1, 1.1)


