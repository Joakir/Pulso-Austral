from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Tabla 1: Rubros (Ej: Gastronomía, Textil, Servicios)
class Rubro(db.Model):
    __tablename__ = 'rubros'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    
    emprendimientos = db.relationship('Emprendimiento', backref='categoria', lazy=True)

    def __repr__(self):
        return f'<Rubro {self.nombre}>'

# Tabla 2: Emprendimientos (La info de los negocios)
class Emprendimiento(db.Model):
    __tablename__ = 'emprendimientos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    contacto = db.Column(db.String(100), nullable=False)
    zona = db.Column(db.String(50)) # Ej: Chacra II, Centro, Margen Sur
    
    # Conexión con la tabla Rubros
    rubro_id = db.Column(db.Integer, db.ForeignKey('rubros.id'), nullable=False)

    def __repr__(self):
        return f'<Emprendimiento {self.nombre}>'