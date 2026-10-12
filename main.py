from db.inicializate_db import inicializate_db
from services.lote_service import Lote_Service
from services.mortalidad_service import mortalidad_service
inicializate_db()
lotes = Lote_Service().getAllLotes()
mortalidad = mortalidad_service().insert_mortalidad()
mortalidad =mortalidad_service().getMortalidad()
for lote in lotes:
    print(dict(lote))

for muertes in mortalidad:
    print(dict(muertes))