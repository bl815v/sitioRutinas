from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL 

from Logic.Usuario import Usuario
from Logic.PlanificadorRutinas import PlanificadorRutinas
from Data.GestorUsuarios import GestorUsuarios

app=Flask(__name__, template_folder='Web', static_folder='Web')
app.secret_key = 'clave'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '#151709Jebl'
app.config['MYSQL_DB'] = 'pruebagym'

mysql = MySQL(app)

gestordeusuarios = GestorUsuarios(mysql)

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/registro')
def pagRegistro():
    return render_template('registro.html')


@app.route('/RegistroExitoso', methods=['POST'])
def RegistroExitoso():
    user1 = Usuario(request.form.get('nombre'), 
                request.form.get('id'), 
                request.form.get('cel'),
                request.form.get('mail'), 
                request.form.get('altura'), 
                request.form.get('peso'),
                request.form.getlist('dias'), 
                request.form.get('objetivo'),
                {})
    
    planificador = PlanificadorRutinas(user1)    
    user1.setRutina(planificador.getEjerciciosxDia())
    gestordeusuarios.guardarUsuario(user1)
    
    return "¡Registro exitoso! Los datos se han guardado en la base de datos."


@app.route('/login', methods=['POST'])
def login():
    correo = request.form.get('mail')
    clave = request.form.get('clave')

    usuario = gestordeusuarios.validarCredenciales(correo, clave)

    if usuario:
        usuarioDB = gestordeusuarios.getUsuarioxMailClave(correo, clave)
        if usuarioDB:
            session['usuario'] = {
                'nombre': usuarioDB.getNombre(),
                'id': usuarioDB.getDocumento(),
                'celular': usuarioDB.getCelular(),
                'mail': usuarioDB.getCorreo(),
                'altura': usuarioDB.getAltura(),
                'peso': usuarioDB.getPeso(),
                'dias': usuarioDB.getDias(),
                'objetivo': usuarioDB.getObjetivo(),
                'rutinas': usuarioDB.getRutina()
            }
            return redirect(url_for('pagRutina'))
        else:
            return "Usuario no encontrado"
    else:
        return "Correo o contraseña incorrectos"


@app.route('/rutina', methods=['GET'])
def pagRutina():
    if 'usuario' in session:
        data = session['usuario']
        return render_template('pagRutina.html', data=data)
    else:
        return "Usuario no encontrado"


@app.route('/usuarios')
def mostrarUsuarios():
    usuarios = gestordeusuarios.getUsuarios()
    return render_template('usuariosRegistrados.html', usuarios=usuarios)


@app.route('/borrarUsuario/<int:usuarioId>', methods=['POST'])
def borrarUsuario(usuarioId):
    gestordeusuarios.borrarUsuario(usuarioId)
    return redirect(url_for('mostrarUsuarios'))


@app.route('/actualizarUsuario/<int:usuarioId>', methods=['POST'])
def actualizarUrsuario(usuarioId):
    try:
        nombre = request.json.get('nombre')
        documento = request.json.get('documento')
        celular = request.json.get('celular')
        correo = request.json.get('correo')
        altura = request.json.get('altura')
        peso = request.json.get('peso')
        dias = request.json.get('dias')
        objetivo = request.json.get('objetivo')
        
        userActualizado = gestordeusuarios.getUsuarioxId(usuarioId)
        userActualizado.setNombre(nombre)
        userActualizado.setDocumento(documento)
        userActualizado.setCelular(celular)
        userActualizado.setCorreo(correo)
        userActualizado.setAltura(altura)
        userActualizado.setPeso(peso)
        userActualizado.setDias(dias)
        userActualizado.setObjetivo(objetivo)
        
        planificador = PlanificadorRutinas(userActualizado)    
        userActualizado.setRutina(planificador.getEjerciciosxDia())
        gestordeusuarios.guardarUsuario(userActualizado)

        return 'Usuario actualizado exitosamente', 200
    except Exception as e:
        return 'Error al actualizar el usuario', 500


if __name__=='__main__':
    app.run(debug=True, port=5000)