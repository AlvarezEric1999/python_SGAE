
from repositories.lote_repository import Lote_Repository

class Lote_Service:
    def __init__(self):
        self.repository = Lote_Repository()

    def getAllLotes(self):
        return self.repository.getLotes()

    def createLote(self):
        return self.repository.createLote()