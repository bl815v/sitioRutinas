from Logic.RutinaG import RutinaG

class RutinaLarson(RutinaG):
    def __init__(self):
        super().__init__() 

        self._dia1 = {'Press de pierna': '4 series de 8 repeticiones',
                      'Press de banca inclinado': '4 series de 8 repeticiones',
                      'Pull-over con mancuerna': '3 series de 10 repeticiones'}
        
        self._dia2 = {'Estiramientos dinámicos': '30-45 minutos'}
        
        self._dia3 = {'Sentadillas búlgaras': '4 series de 8 repeticiones',
                      'Fondos en paralelas': '4 series de 8 repeticiones',
                      'Elevaciones frontales con barra': '3 series de 10 repeticiones'}
        
        self._dia4 = {'Caminata en cuesta': '30-45 minutos'}
        
        self._dia5 = {'Prensa de hombros': '4 series de 8 repeticiones',
                      'Curl de bíceps con barra Z': '4 series de 8 repeticiones',
                      'Extensiones de tríceps con barra': '3 series de 10 repeticiones'}
        
        self._dia6 = {'Yoga o Tai Chi': '30-45 minutos'}
        
        self._dia7 = {'Peso muerto sumo': '4 series de 8 repeticiones',
                      'Dominadas pronas': '4 series de 8 repeticiones',
                      'Flexiones diamante': '3 series de 10 repeticiones'}

