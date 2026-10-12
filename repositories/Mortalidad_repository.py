from db.connection import createConnection

class Mortalidad_repository():
    def __init__(self):
        self.conection = createConnection()

    def created_mortaliad(self):
        try:

            lote = self.conection.execute( "SELECT id_lote FROM lotes LIMIT 1" ).fetchone()
            id_lote = lote["id_lote"]

            registros = [
            (
                id_lote,
                1,
                "2026-10-05",
               
            ),
            (
                id_lote,
                2,
                "2026-10-07",
               
            ),
            (
                id_lote,
                1,
                "2026-10-09",
                
            )
        ]

            cursor = self.conection.executemany(
                """
            INSERT INTO mortalidad (
                id_lote,
                cantidad_muertos,
                fecha
               
            )
            VALUES (?, ?, ?)
        """, registros
            )
            self.conection.commit()
            print("datos ingresados")


        finally:
            self.conection.close()

    def get_mortalidad(self):
        try:
            cursor = self.conection.execute("SELECT * FROM Mortalidad")
            return cursor.fetchall()
        finally:
            self.conection.close()
