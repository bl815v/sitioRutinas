import random

class ListaRutinas:
    def __init__(self, rutinas):
        self._rutinas = rutinas

    def getOpcionesRutinas(self):
        opciones = []
        for rutina in self._rutinas:
            opciones.append((rutina.getDia1(), rutina.getDia2(), rutina.getDia3(),
                             rutina.getDia4(), rutina.getDia5(), rutina.getDia6(), rutina.getDia7()))
        return opciones

    def getEjerciciosPorDia(self, dias):
        numeroDias = {'Lunes': 1, 'Martes': 2, 'Miércoles': 3, 'Jueves': 4, 'Viernes': 5, 'Sábado': 6, 'Domingo': 7}

        rutinaSelect = random.choice(self._rutinas)

        ejerciciosxDia = {}
        for dia in dias:
            diaNumero = numeroDias[dia]
            ejerciciosxDia[dia] = getattr(rutinaSelect, f'_dia{diaNumero}')

        return ejerciciosxDia