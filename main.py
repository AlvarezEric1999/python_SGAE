from db.inicializate_db import inicializate_db
from services.lote_service import Lote_Service

inicializate_db()
lotes = Lote_Service().getAllLotes()
#Lote_Service().createLote()
for lote in lotes:
    print(lote["codigo"])