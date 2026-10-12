from db.connection import createConnection


class Lote_Repository():

        def __init__(self):
            self.connection = createConnection()

        def createLote(self):
            try:
              cursor = self.connection.execute("""
                  INSERT INTO lotes (
                      codigo,
                      nombre,
                      cantidad_inicial,
                      fecha_ingreso,
                      estado
                  )
                  VALUES (?, ?, ?, ?, ?)
              """, (
                  "LT-2026-10-001",
                  "Lote de prueba",
                  20,
                  "2026-10-11",
                  "Activo"
              ))
              self.connection.commit()
              print("Lote insertado correctamente.") 
            finally:
              self.connection.close()

        
        def getLotes(self):
          try:
            cursor = self.connection.execute(
                     "SELECT * FROM lotes"
                     )
            return cursor.fetchall()
        
          finally:
               self.connection.close()
    