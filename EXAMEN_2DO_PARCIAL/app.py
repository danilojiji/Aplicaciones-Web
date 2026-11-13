# LIBRERÍAS
from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL

# CREAR APLICACIÓN
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
    
# CONEXION A MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud_directorio'

app.secret_key = 'mysecretkey'

# INICIALIZAR LA CONEXIÓN
mysql = MySQL(app)

# RUTA PRINCIPAL: RED
@app.route('/')
def index():
    return render_template('index.html', listDirectorio= conDirectorio)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo = request.form['correo']
        direccion = request.form['direccion']
        print(nombre,apellido,telefono,correo,direccion)

        # CONEXION CON LA BD Y EJECUCION DE INSERT
        con = mysql.connection.cursor()
        con.execute("INSERT INTO tb_directorio(nombre, apellido, telefono, correo, direccion) VALUES (%s, %s, %s, %s, %s)", (nombre, apellido, telefono, correo, direccion))
        mysql.connection.commit()
    flash('Contacto agregado correctamente')
    return 'Los datos llegaron!'


# EJECUTAR APLICACION
if __name__ == "__main__":
    app.run(debug=True)