from Logic.ListaRutinas import ListaRutinas
from Logic.RutinaP import RutinaP
from Logic.RutinaPhoenix import RutinaPhoenix

class ListaRutinasP(ListaRutinas):
    def __init__(self):
        super().__init__([
            RutinaPhoenix()
        ])