from Logic.ListaRutinasG import ListaRutinasG
from Logic.ListaRutinasP import ListaRutinasP
from Logic.ListaRutinasM import ListaRutinasM

class PlanificadorRutinas:
    """Clase para planificar rutinas de ejercicios según el objetivo del usuario.

    Args:
        user (Usuario): Un objeto Usuario que representa al usuario para el que se planificarán las rutinas.

    Attributes:
        user (Usuario): El usuario para el que se planificarán las rutinas.

    """

    def __init__(self, user):
        """Inicializa PlanificadorRutinas con el usuario dado.

        Args:
            user (Usuario): Un objeto Usuario que representa al usuario para el que se planificarán las rutinas.

        """
        self.user = user

    def getEjerciciosxDia(self):
        """Obtiene los ejercicios planificados para cada día según el objetivo del usuario.

        Returns:
            dict: Un diccionario que relaciona cada día con los ejercicios correspondientes.

        Raises:
            ValueError: Si el objetivo del usuario no es válido.

        """
        objetivo = self.user.getObjetivo()
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        if objetivo == "subir de peso":
            listaRutinas = ListaRutinasG()
        elif objetivo == "bajar de peso":
            listaRutinas = ListaRutinasP()
        elif objetivo == "mantener tu peso":
            listaRutinas = ListaRutinasM()
        else:
            raise ValueError("Objetivo no válido")
        
        return listaRutinas.getEjerciciosPorDia(dias) #self.user.getDias() para solo los seleccionados