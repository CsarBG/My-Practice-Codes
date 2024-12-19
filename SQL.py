import sqlite3

miConexion=sqlite3.connect("DBD.db")
miCursor=miConexion.cursor()

miCursor.execute('DELETE FROM DLC')
miCursor.execute('DELETE FROM Killers')
miCursor.execute('DELETE FROM Survivors')

miConexion.commit()
miConexion.close()