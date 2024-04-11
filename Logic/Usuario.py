
class Usuario:
    def __init__(self, nombre, documento, celular, correo, altura, peso, dias, objetivo):
        self._nombre = nombre
        self._documento = documento
        self._celular = celular
        self._correo = correo
        self._altura = altura
        self._peso = peso
        self._dias = dias
        self.setObjetivo(objetivo)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getDocumento(self):
        return self._documento

    def setDocumento(self, documento):
        self._documento = documento

    def getCelular(self):
        return self._celular

    def setCelular(self, celular):
        self._celular = celular

    def getCorreo(self):
        return self._correo

    def setCorreo(self, correo):
        self._correo = correo

    def getAltura(self):
        return self._altura

    def setAltura(self, altura):
        self._altura = altura

    def getPeso(self):
        return self._peso

    def setPeso(self, peso):
        self._peso = peso

    def getDias(self):
        return self._dias

    def setDias(self, dias):
        self._dias = dias

    def getObjetivo(self):
        return self._objetivo

    def setObjetivo(self, objetivo):
        if(objetivo == "perderPeso"):
            objetivo = "bajar de peso"
        elif(objetivo == "ganarPeso"):
            objetivo = "subir de peso"
        elif(objetivo == "mantenerPeso"):
            objetivo = "mantener tu peso"
        else:
            raise ValueError("Objetivo no válido")
        self._objetivo = objetivo