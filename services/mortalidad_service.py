from repositories.Mortalidad_repository import Mortalidad_repository

class mortalidad_service():
    def __init__(self):
        self.mortalidad = Mortalidad_repository()

    def insert_mortalidad(self):
        return self.mortalidad.created_mortaliad()

    def getMortalidad(self):
        return self.mortalidad.get_mortalidad()
