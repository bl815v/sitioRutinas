
class Usuario:
    """Clase para representar a un usuario del gym.

    Args:
        nombre (str): El nombre del usuario.
        documento (str): El número de documento del usuario.
        celular (str): El número de celular del usuario.
        correo (str): El correo electrónico del usuario.
        altura (float): La altura del usuario en centímetros.
        peso (float): El peso del usuario en kilogramos.
        dias (list): Una lista que representa los días en los que el usuario entrena.
        objetivo (str): El objetivo del usuario, puede ser "perderPeso", "ganarPeso" o "mantenerPeso".

    Attributes:
        _nombre (str): El nombre del usuario.
        _documento (str): El número de documento del usuario.
        _celular (str): El número de celular del usuario.
        _correo (str): El correo electrónico del usuario.
        _altura (float): La altura del usuario en centímetros.
        _peso (float): El peso del usuario en kilogramos.
        _dias (list): Una lista que representa los días en los que el usuario entrena.
        _objetivo (str): El objetivo del usuario, puede ser "perderPeso", "ganarPeso" o "mantenerPeso".

    """

    def __init__(self, nombre, documento, celular, correo, altura, peso, dias, objetivo):
        """Inicializa un objeto Usuario con los datos proporcionados.

        Args:
            nombre (str): El nombre del usuario.
            documento (str): El número de documento del usuario.
            celular (str): El número de celular del usuario.
            correo (str): El correo electrónico del usuario.
            altura (float): La altura del usuario en centímetros.
            peso (float): El peso del usuario en kilogramos.
            dias (list): Una lista que representa los días en los que el usuario entrena.
            objetivo (str): El objetivo del usuario, puede ser "perderPeso", "ganarPeso" o "mantenerPeso".

        Raises:
            ValueError: Si el objetivo proporcionado no es válido.

        """
        self._nombre = nombre
        self._documento = documento
        self._celular = celular
        self._correo = correo
        self._altura = altura
        self._peso = peso
        self._dias = dias
        self.setObjetivo(objetivo)

    def getNombre(self):
        """Obtiene el nombre del usuario.

        Returns:
            str: El nombre del usuario.

        """
        return self._nombre

    def setNombre(self, nombre):
        """Establece el nombre del usuario.

        Args:
            nombre (str): El nuevo nombre del usuario.

        """
        self._nombre = nombre

    def getDocumento(self):
        """Obtiene el número de documento del usuario.

        Returns:
            str: El número de documento del usuario.

        """
        return self._documento

    def setDocumento(self, documento):
        """Establece el número de documento del usuario.

        Args:
            documento (str): El nuevo número de documento del usuario.

        """
        self._documento = documento

    def getCelular(self):
        """Obtiene el número de celular del usuario.

        Returns:
            str: El número de celular del usuario.

        """
        return self._celular

    def setCelular(self, celular):
        """Establece el número de celular del usuario.

        Args:
            celular (str): El nuevo número de celular del usuario.

        """
        self._celular = celular

    def getCorreo(self):
        """Obtiene el correo electrónico del usuario.

        Returns:
            str: El correo electrónico del usuario.

        """
        return self._correo

    def setCorreo(self, correo):
        """Establece el correo electrónico del usuario.

        Args:
            correo (str): El nuevo correo electrónico del usuario.

        """
        self._correo = correo

    def getAltura(self):
        """Obtiene la altura del usuario.

        Returns:
            float: La altura del usuario en centímetros.

        """
        return self._altura

    def setAltura(self, altura):
        """
        Establece la altura del usuario.

        Args:
            altura (float): La nueva altura del usuario en centímetros.

        """
        self._altura = altura

    def getPeso(self):
        """Obtiene el peso del usuario.

        Returns:
            float: El peso del usuario en kilogramos.

        """
        return self._peso

    def setPeso(self, peso):
        """Establece el peso del usuario.

        Args:
            peso (float): El nuevo peso del usuario en kilogramos.

        """
        self._peso = peso

    def getDias(self):
        """Obtiene los días en los que el usuario entrena.

        Returns:
            list: Una lista de los días en los que el usuario entrena.

        """
        return self._dias

    def setDias(self, dias):
        """Establece los días en los que el usuario entrena.

        Args:
            dias (list): Una lista de cadenas que representan los días en los que el usuario entrena.

        """
        self._dias = dias

    def getObjetivo(self):
        """Obtiene el objetivo del usuario.

        Returns:
            str: El objetivo del usuario.

        """
        return self._objetivo

    def setObjetivo(self, objetivo):
        """Establece el objetivo del usuario.

        Args:
            objetivo (str): El nuevo objetivo del usuario.

        Raises:
            ValueError: Si el objetivo proporcionado no es válido.

        """
        if(objetivo == "perderPeso"):
            objetivo = "bajar de peso"
        elif(objetivo == "ganarPeso"):
            objetivo = "subir de peso"
        elif(objetivo == "mantenerPeso"):
            objetivo = "mantener tu peso"
        else:
            raise ValueError("Objetivo no válido")
        self._objetivo = objetivo