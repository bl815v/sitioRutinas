from Logic.ListaRutinas import ListaRutinas
from Logic.RutinaBrolin import RutinaBrolin
from Logic.RutinaLarson import RutinaLarson

class ListaRutinasG(ListaRutinas):
    """Clase para manejar una lista de rutinas de ejercicios específicas para ganar peso.

    Esta clase hereda de ListaRutinas y proporciona una lista predefinida de rutinas para ganar peso.

    """

    def __init__(self):
        """Inicializa ListaRutinasG con una lista predefinida de rutinas para ganar peso.

        """
        super().__init__([
            #RutinaBrolin(),
            RutinaLarson()
        ])