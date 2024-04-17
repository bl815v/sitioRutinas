
class Rutina:
    """Clase base para definir una rutina de ejercicios.

    Esta clase proporciona métodos para acceder y establecer los ejercicios para cada día de la semana.

    """    
    def __init__(self):
        """Inicializa Rutina con valores nulos para los ejercicios de cada día.

        """
        self._dia1 = None
        self._dia2 = None
        self._dia3 = None
        self._dia4 = None
        self._dia5 = None
        self._dia6 = None
        self._dia7 = None

    def getDia1(self):
        """Obtiene los ejercicios para el primer día de la semana.

        Returns:
            dict: Un diccionario que contiene los ejercicios para el primer día.

        """
        return self._dia1

    def setDia1(self, value):
        """Establece los ejercicios para el primer día de la semana.

        Args:
            value (dict): Un diccionario que contiene los ejercicios para el primer día.

        """
        self._dia1 = value

    def getDia2(self):
        """Obtiene los ejercicios para el segundo día de la semana.

        Returns:
            dict: Un diccionario que contiene los ejercicios para el segundo día.

        """
        return self._dia2

    def setDia2(self, value):
        """Establece los ejercicios para el segundo día de la semana.

        Args:
            value (dict): Un diccionario que contiene los ejercicios para el segundo día.

        """
        self._dia2 = value

    def getDia3(self):
        """Obtiene los ejercicios para el tercer día de la semana.

        Returns:
            dict: Un diccionario que contiene los ejercicios para el tercer día.

        """
        return self._dia3

    def setDia3(self, value):
        """Establece los ejercicios para el tercer día de la semana.

        Args:
            value (dict): Un diccionario que contiene los ejercicios para el tercer día.

        """
        self._dia3 = value

    def getDia4(self):
        """Obtiene los ejercicios para el cuarto día de la semana.

        Returns:
            dict: Un diccionario que contiene los ejercicios para el cuarto día.

        """
        return self._dia4

    def setDia4(self, value):
        """Establece los ejercicios para el cuarto día de la semana.

        Args:
            value (dict): Un diccionario que contiene los ejercicios para el cuarto día.

        """
        self._dia4 = value

    def getDia5(self):
        """Obtiene los ejercicios para el quinto día de la semana.

        Returns:
            dict: Un diccionario que contiene los ejercicios para el quinto día.

        """
        return self._dia5

    def setDia5(self, value):
        """Establece los ejercicios para el quinto día de la semana.

        Args:
            value (dict): Un diccionario que contiene los ejercicios para el quinto día.

        """
        self._dia5 = value

    def getDia6(self):
        """Obtiene los ejercicios para el sexto día de la semana.

        Returns:
            dict: Un diccionario que contiene los ejercicios para el sexto día.

        """
        return self._dia6

    def setDia6(self, value):
        """Establece los ejercicios para el sexto día de la semana.

        Args:
            value (dict): Un diccionario que contiene los ejercicios para el sexto día.

        """
        self._dia6 = value

    def getDia7(self):
        """Obtiene los ejercicios para el séptimo día de la semana.

        Returns:
            dict: Un diccionario que contiene los ejercicios para el séptimo día.

        """
        return self._dia7

    def setDia7(self, value):
        """Establece los ejercicios para el séptimo día de la semana.

        Args:
            value (dict): Un diccionario que contiene los ejercicios para el séptimo día.

        """        
        self._dia7 = value
