from flask import Flask, render_template, request, session

from Logic.Usuario import Usuario
from Logic.PlanificadorRutinas import PlanificadorRutinas

app=Flask(__name__, template_folder='Web', static_folder='Web')
app.secret_key = 'clave'

@app.route('/')
def index():
    return render_template('index.html')

data = {}
@app.route('/rutina', methods=['POST'])
def pagRutina():
    user1 = Usuario(request.form.get('nombre'), 
                request.form.get('id'), 
                request.form.get('cel'),
                request.form.get('mail'), 
                request.form.get('altura'), 
                request.form.get('peso'),
                request.form.getlist('dias'), 
                request.form.get('objetivo'))
    
    planificador = PlanificadorRutinas(user1)

    data = {
        'nombre': user1.getNombre(),
        'id': user1.getDocumento(),
        'celular': user1.getCelular(),
        'mail': user1.getCorreo(),
        'altura': user1.getAltura(),
        'peso': user1.getPeso(),
        'dias': user1.getDias(),
        'objetivo': user1.getObjetivo(),
        'rutinas': planificador.getEjerciciosxDia()
    }
    session.update(data)
    print(user1.getObjetivo())
    
    return render_template('pagRutina.html', data=data)


if __name__=='__main__':
    app.run(debug=True, port=5000)