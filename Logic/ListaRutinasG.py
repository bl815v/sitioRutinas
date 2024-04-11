from Logic.ListaRutinas import ListaRutinas
from Logic.RutinaG import RutinaG
from Logic.RutinaBrolin import RutinaBrolin
from Logic.RutinaLarson import RutinaLarson

class ListaRutinasG(ListaRutinas):
    def __init__(self):
        super().__init__([
            #RutinaBrolin(),
            RutinaLarson()
        ])