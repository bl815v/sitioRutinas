from Logic.ListaRutinas import ListaRutinas
from Logic.RutinaLiu import RutinaLiu

class ListaRutinasM(ListaRutinas):
    """Clase para manejar una lista de rutinas de ejercicios específicas para mantener peso.

    Esta clase hereda de ListaRutinas y proporciona una lista predefinida de rutinas para mantener peso.

    """
    
    def __init__(self):
        """Inicializa ListaRutinasM con una lista predefinida de rutinas para mantener peso.

        """
        super().__init__([
            RutinaLiu()
        ])
