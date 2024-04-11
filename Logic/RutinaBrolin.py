from Logic.RutinaG import RutinaG

class RutinaBrolin(RutinaG):
    def __init__(self):
        super().__init__()

        self._dia1 = {'Sentadillas con peso': '4 series de 8 repeticiones',
                      'Press de banca': '4 series de 8 repeticiones',
                      'Peso muerto': '3 series de 10 repeticiones'}
        
        self._dia2 = {'Yoga o estiramientos': '30-45 minutos'}
        
        self._dia3 = {'Press militar': '4 series de 8 repeticiones',
                      'Remo con barra': '4 series de 8 repeticiones',
                      'Elevaciones laterales': '3 series de 10 repeticiones'}
        
        self._dia4 = {'Caminata ligera': '30-45 minutos'}
        
        self._dia5 = {'Sentadillas frontales': '4 series de 8 repeticiones',
                      'Press de hombros con mancuernas': '4 series de 8 repeticiones',
                      'Curl de bíceps': '3 series de 10 repeticiones'}
        
        self._dia6 = {'Pilates o estiramientos': '30-45 minutos'}
        
        self._dia7 = {'Peso muerto rumano': '4 series de 8 repeticiones',
                      'Dominadas o polea al pecho': '4 series de 8 repeticiones',
                      'Tríceps con polea': '3 series de 10 repeticiones'}
