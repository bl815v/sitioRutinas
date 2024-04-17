from Logic.ListaRutinas import ListaRutinas
from Logic.RutinaPhoenix import RutinaPhoenix

class ListaRutinasP(ListaRutinas):
    """Clase para manejar una lista de rutinas de ejercicios específicas para ganar peso.

    Esta clase hereda de ListaRutinas y proporciona una lista predefinida de rutinas para ganar peso.

    """

    def __init__(self):
        """Inicializa ListaRutinasP con una lista predefinida de rutinas para perder peso.

        """
        super().__init__([
            RutinaPhoenix()
        ])