
from Logic.RutinaM import RutinaM

class RutinaLiu(RutinaM):
    """Clase para definir una rutina de ejercicios específica para mantener peso, basada en la rutina de Liu.

    Esta clase hereda de RutinaM y define una rutina de ejercicios completa para mantener peso.

    """

    def __init__(self):
        """Inicializa RutinaLiu con una serie de ejercicios específicos para cada día de la semana.

        """
        super().__init__()

        self._dia1 = {'Caminata rápida': '30 minutos', 
                    'Estiramientos': '10 minutos'}
        
        self._dia2 = {'Sentadillas': '3 series de 12 repeticiones',
                    'Flexiones de brazos': '3 series de 12 repeticiones',
                    'Levantamiento de pesas': '3 series de 12 repeticiones'}
        
        self._dia3 = {'Yoga o Pilates': '30 minutos',
                    'Estiramientos': '10 minutos'}
        
        self._dia4 = {'Bicicleta estática o elíptica': '30 minutos',
                    'Estiramientos': '10 minutos'}
        
        self._dia5 = {'Zancadas': '3 series de 12 repeticiones',
                    'Flexiones de brazos': '3 series de 12 repeticiones',
                    'Abdominales': '3 series de 12 repeticiones'}
        
        self._dia6 = {'Natación o aeróbicos': '30 minutos',
                    'Estiramientos': '10 minutos'}
        
        self._dia7 = {'Caminata ligera': '30-45 minutos'}
