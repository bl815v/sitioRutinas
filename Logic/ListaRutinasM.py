from Logic.ListaRutinas import ListaRutinas
from Logic.RutinaM import RutinaM
from Logic.RutinaLiu import RutinaLiu

class ListaRutinasM(ListaRutinas):
    def __init__(self):
        super().__init__([
            RutinaLiu()
        ])
