import random

class ListaRutinas:
    """Clase para manejar una lista de rutinas de ejercicios.
    
    Args:
        rutinas (list): Una lista de objetos Rutina.  
    
    Attributes:
        _rutinas (list): La lista de rutinas de ejercicios.

    """

    def __init__(self, rutinas):
        """Inicializa ListaRutinas con la lista de rutinas dada.
        
        Args:
            rutinas (list): Una lista de objetos Rutina.  

        """
        self._rutinas = rutinas


    def getOpcionesRutinas(self):
        """Obtiene las opciones de rutinas disponibles.

        Returns:
            list: Una lista de tuplas que contienen los días de la semana para cada rutina.

        """
        opciones = []
        for rutina in self._rutinas:
            opciones.append((rutina.getDia1(), rutina.getDia2(), rutina.getDia3(),
                             rutina.getDia4(), rutina.getDia5(), rutina.getDia6(), rutina.getDia7()))
        return opciones


    def getEjerciciosPorDia(self, dias):
        """Obtiene los ejercicios para cada día especificado.

        Args:
            dias (list): Una lista de los días de la semana en los que se hará la rutina.

        Returns:
            dict: Un diccionario que relaciona cada día con los ejercicios correspondientes.

        """
        numeroDias = {'Lunes': 1, 'Martes': 2, 'Miércoles': 3, 'Jueves': 4, 'Viernes': 5, 'Sábado': 6, 'Domingo': 7}

        rutinaSelect = random.choice(self._rutinas)

        ejerciciosxDia = {}
        for dia in dias:
            diaNumero = numeroDias[dia]
            ejerciciosxDia[dia] = getattr(rutinaSelect, f'_dia{diaNumero}')

        return ejerciciosxDia