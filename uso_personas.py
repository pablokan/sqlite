from personas import CrudSQLite

crud = CrudSQLite('personas.db') # crea o abre
crud.crear_tabla()
crud.agregar('Juan', 25)
crud.agregar('Pedro', 30)
crud.listar()
print('Modifico registro #2')
crud.modificar(2, 'Pedrito', 46)
crud.listar()
print('Elimino registro #1')
crud.eliminar(1)
crud.listar()
crud.cerrar_db()
