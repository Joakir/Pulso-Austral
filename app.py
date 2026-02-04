from flask import Flask, render_template, request, redirect, url_for
from models import db, Emprendimiento, Rubro


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    todos_los_negocios = Emprendimiento.query.all()

    return render_template('index.html', lista_emprendimientos=todos_los_negocios)


@app.route('/crear', methods=['GET', 'POST'])
def crear_emprendimiento():
    if request.method == 'POST':
        nombre = request.form['nombre_form']
        desc = request.form['descripcion_form']
        cont = request.form['contacto_form']
        zona = request.form['zona_form']
        rubro_id = request.form['rubro_id_form']

        nuevo_negocio = Emprendimiento(
            nombre=nombre,
            descripcion=desc,
            contacto=cont,
            zona=zona,
            rubro_id=rubro_id
        )

        db.session.add(nuevo_negocio)
        db.session.commit()

        return redirect('/')

    rubros_disponibles = Rubro.query.all()
    return render_template('crear.html', lista_rubros=rubros_disponibles)


@app.route('/borrar/<int:id>')
def borrar_emprendimiento(id):
    emprendimiento_a_borrar = Emprendimiento.query.get_or_404(id)
    db.session.delete(emprendimiento_a_borrar)
    db.session.commit()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)