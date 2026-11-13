#importamos los paquetes flask
from flask import Flask, render_template, request

#importar las funciones para generar hashes de la contrasena y comprobar si una contrasena coincide con el hash
from werkzeug.security import generate_password_hash, check_password_hash
#creamos una instancia de nuestra aplicacion
app = Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'FlaskDB'

#Permite que Flask vuelva a cargar las plantillas cuando se modifican
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'mysecretkey'

#Creacion de ruta. la ruta/ es la ruta raiz, sera la que mostrara cuando el proyecto
@app.route("/")
def home():
    return render_template("login.html")

""" @app.route("/registro", method=["GET", ["POST"]])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido_p = request.form["apellido_p"]
        apellido_m = request.form["apellido_m"]
        correo = request.form["correo"]
        password_hash = request.form["passwrod_hash"]
        id_rol = request.form["id_rol"]

        password_hasheada = generate_password_hash(password_hash)
 """
#iniciamos el servidor FLASK en el puerto 5000
if __name__ == "__main__":
    app.run(port=5000)