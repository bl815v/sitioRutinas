from Logic.RutinaP import RutinaP

class RutinaPhoenix(RutinaP):
    def __init__(self):
        super().__init__()     
        self._dia1 = {'Carrera continua o bicicleta estática': '45 minutos',
                        'Abdominales y estiramientos': '10 minutos'}
        
        self._dia2 = {'Intervalos de sprints y caminatas rápidas': '30 minutos',
                        'Estiramientos': '10 minutos'}
        
        self._dia3 = {'Sentadillas': '3 series de 12 repeticiones',
                    'Flexiones de brazos': '3 series de 12 repeticiones',
                    'Peso muerto': '3 series de 12 repeticiones'}
        
        self._dia4 = {'Aeróbicos o baile': '45 minutos',
                    'Abdominales y estiramientos': '10 minutos'}
        
        self._dia5 = {'Entrenamiento en circuito': '30 minutos',
                    'Estiramientos': '10 minutos'}
        self._dia6 = {'Natación o Remo': '45 minutos',
                    'Abdominales y estiramientos': '10 minutos'}
        self._dia7 = {'Caminata rápida': '45-60 minutos'}
