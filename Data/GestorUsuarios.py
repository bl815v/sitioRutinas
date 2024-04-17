
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

        cur.execute("INSERT INTO usuarios (nombre, documento, celular, correo, altura, peso, dias, objetivo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (usuario.getNombre(), usuario.getDocumento(), usuario.getCelular(), usuario.getCorreo(), usuario.getAltura(), usuario.getPeso(), dias_seleccionados, usuario.getObjetivo()))

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
        