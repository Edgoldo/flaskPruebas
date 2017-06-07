from flask import Flask
from flask import render_template

"""!
Se crea un nuevo objeto.
template_folder: carpeta donde se encuentran los templates, por defecto el nombre
de esta carpeta es templates
"""
app = Flask(__name__, template_folder = "templates")

"""!
Wrap o decorador, se especifica la ruta en la que se va a 
ejecutar la función index
"""

@app.route('/principal/<parm1>/<int:parm2>')
# Se crea una función a ejecutar sobre la url
def index(parm1 = None, parm2 = None):
	"""!
	Hace el llamado al template que se encuentra en la carpeta templates,
	la cual debe encontrarse al mismo nivel que este archivo
	"""
	return render_template('prueba5_1.html', usuario=parm1, dato2=parm2)
	
if __name__ == '__main__':
	"""!
	Se ejecuta el servidor, el puerto por defecto es el 5000
	se usa debug en True para poder detectar los cambios realizados
	sobre el proyecto sin necesidad de ejecutar nuevamente el proyecto
	"""
	app.run(debug = True, port = 8080)