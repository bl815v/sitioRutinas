import json

from Logic.Usuario import Usuario


class GestorUsuarios:
    """Clase para gestionar usuarios en una base de datos.

    Args:
        db: Objeto que representa la conexión a la base de datos.

    Attributes:
        db: Objeto que representa la conexión a la base de datos.

    """

    def __init__(self, db):
        """Inicializa GestorUsuarios con la conexión a la base de datos.

        Args:
            db: Objeto que representa la conexión a la base de datos.

        """
        self.db = db

    def guardarUsuario(self, usuario):
        """Guarda un usuario en la base de datos.

        Args:
            usuario (Usuario): El usuario a guardar en la base de datos.

        """
        cur = self.db.connection.cursor()

        dias_seleccionados = ', '.join(usuario.getDias())

        cur.execute("INSERT INTO usuarios (nombre, documento, celular, correo, altura, peso, dias, objetivo, rutina) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (usuario.getNombre(), usuario.getDocumento(), usuario.getCelular(), usuario.getCorreo(), usuario.getAltura(), usuario.getPeso(), dias_seleccionados, usuario.getObjetivo(), json.dumps(usuario.getRutina(), ensure_ascii=False)))

        self.db.connection.commit()
        cur.close()    

    def borrarUsuario(self, idUsuario):
        """Borra un usuario de la base de datos.

        Args:
            idUsuario (int): El ID del usuario a borrar.

        """
        cur = self.db.connection.cursor()
        cur.execute("DELETE FROM usuarios WHERE id = %s", (idUsuario,))
        self.db.connection.commit()
        cur.close()

    def getUsuarios(self):
        """Obtiene todos los usuarios almacenados en la base de datos.

        Returns:
            list: Una lista con los usuarios almacenados en la base de datos.

        """
        cur = self.db.connection.cursor()
        cur.execute("SELECT * FROM usuarios")
        usuarios = cur.fetchall()
        cur.close()
        return usuarios
    
    def validarCredenciales(self, correo, clave):
        """Valida las credenciales de un usuario.

        Args:
            correo (str): El correo del usuario.
            clave (str): La contraseña del usuario.

        Returns:
            dict or None: Un diccionario con los datos del usuario si las credenciales son válidas,
                            None si las credenciales son inválidas.

        """
        cur = self.db.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE correo = %s AND documento = %s", (correo, clave))
        usuario = cur.fetchone()
        cur.close()

        return usuario if usuario else None
    
    def getUsuarioxMailClave(self, correo, clave):
        """Obtiene un usuario de la base de datos según su correo electrónico y clave.

        Args:
            correo (str): El correo electrónico del usuario.
            clave (str): La clave del usuario.

        Returns:
            Usuario: El objeto Usuario si se encuentra, None si no se encuentra.

        """
        cur = self.db.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE correo = %s AND documento = %s", (correo, clave))
        usuarioData = cur.fetchone()
        cur.close()

        if usuarioData:
            usuario = Usuario(usuarioData[1], 
                            usuarioData[2], 
                            usuarioData[3],
                            usuarioData[4], 
                            usuarioData[5], 
                            usuarioData[6],
                            usuarioData[7], 
                            usuarioData[8],
                            usuarioData[9])
            return usuario
        else:
            return None


    def getUsuarioxDocumento(self, documento):
        """Obtiene un usuario de la base de datos según su documento.

        Args:
            documento (str): El documento del usuario.

        Returns:
            Usuario: El objeto Usuario si se encuentra, None si no se encuentra.

        """
        cur = self.db.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE documento = %s", (documento,))
        usuarioData = cur.fetchone()
        cur.close()

        if usuarioData:
            usuario = Usuario(usuarioData[1], 
                              usuarioData[2], 
                              usuarioData[3],
                              usuarioData[4], 
                              usuarioData[5], 
                              usuarioData[6],
                              usuarioData[7], 
                              usuarioData[8],
                              usuarioData[9])
            return usuario
        else:
            return None

    def getUsuarioxId(self, id):
        """Obtiene un usuario de la base de datos según su id en la base de datos.

        Args:
            id (int): El id del usuario.

        Returns:
            Usuario: El objeto Usuario si se encuentra, None si no se encuentra.

        """
        cur = self.db.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
        usuarioData = cur.fetchone()
        cur.close()

        if usuarioData:
            usuario = Usuario(usuarioData[1], 
                              usuarioData[2], 
                              usuarioData[3],
                              usuarioData[4], 
                              usuarioData[5], 
                              usuarioData[6],
                              usuarioData[7], 
                              usuarioData[8],
                              usuarioData[9])
            return usuario
        else:
            return None
