from db.connection import createConnection

def inicializate_db():
    conection = createConnection()

    try:
        conection.execute("""
            CREATE TABLE IF NOT EXISTS lotes (
                id_lote INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT NOT NULL UNIQUE,
                nombre TEXT NOT NULL,
                cantidad_inicial INTEGER NOT NULL
                    CHECK(cantidad_inicial > 0),
                fecha_ingreso TEXT NOT NULL,
                estado TEXT NOT NULL DEFAULT 'Activo'
            )
        """)


        # Tabla de insumos
        conection.execute("""
            CREATE TABLE IF NOT EXISTS insumos (
                id_insumo INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL CHECK(precio >= 0),
                unidad_medida TEXT NOT NULL
            )
        """)

        # Tabla de mortalidad
        conection.execute("""
            CREATE TABLE IF NOT EXISTS mortalidad (
                id_mortalidad INTEGER PRIMARY KEY AUTOINCREMENT,
                id_lote INTEGER NOT NULL,
                cantidad_muertos INTEGER NOT NULL
                    CHECK(cantidad_muertos > 0),
                fecha TEXT NOT NULL,
                FOREIGN KEY (id_lote)
                    REFERENCES lotes(id_lote)
            )
        """)

        # Tabla de costos por lote
        conection.execute("""
            CREATE TABLE IF NOT EXISTS costos_lote (
                id_costo INTEGER PRIMARY KEY AUTOINCREMENT,
                id_lote INTEGER NOT NULL,
                id_insumo INTEGER NOT NULL,
                cantidad REAL NOT NULL CHECK(cantidad > 0),
                precio_unitario REAL NOT NULL
                    CHECK(precio_unitario >= 0),
                FOREIGN KEY (id_lote)
                    REFERENCES lotes(id_lote),
                FOREIGN KEY (id_insumo)
                    REFERENCES insumos(id_insumo)
            )
        """)

        # Tabla de ventas
        conection.execute("""
            CREATE TABLE IF NOT EXISTS ventas (
                id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
                id_lote INTEGER NOT NULL,
                cantidad INTEGER NOT NULL CHECK(cantidad > 0),
                precio_unitario REAL NOT NULL
                    CHECK(precio_unitario >= 0),
                fecha_venta TEXT NOT NULL,
                FOREIGN KEY (id_lote)
                    REFERENCES lotes(id_lote)
            )
        """)

        conection.commit()

        print("Base de datos inicializada correctamente.")

    except Exception as error:
        conection.rollback()
        print(f"error to inicializate db")

    finally:
        conection.close()
