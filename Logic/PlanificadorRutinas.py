from Logic.ListaRutinasG import ListaRutinasG
from Logic.ListaRutinasP import ListaRutinasP
from Logic.ListaRutinasM import ListaRutinasM

class PlanificadorRutinas:
    def __init__(self, user):
        self.user = user

    def getEjerciciosxDia(self):
        objetivo = self.user.getObjetivo()
        if objetivo == "subir de peso":
            listaRutinas = ListaRutinasG()
        elif objetivo == "bajar de peso":
            listaRutinas = ListaRutinasP()
        elif objetivo == "mantener tu peso":
            listaRutinas = ListaRutinasM()
        else:
            raise ValueError("Objetivo no válido")
        
        return listaRutinas.getEjerciciosPorDia(self.user.getDias())