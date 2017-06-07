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
@app.route('/')
@app.route('/principal/')
@app.route('/principal/<parm1>')
@app.route('/principal/<parm1>/<int:parm2>')
# Se crea una función a ejecutar sobre la url
def index(parm1 = None, parm2 = 3):
	"""!
	Hace el llamado al template que se encuentra en la carpeta templates,
	la cual debe encontrarse al mismo nivel que este archivo
	"""
	diccionario = {'Fruta1': 'manzana', 'Fruta2': 'pera'}
	if parm1 and parm2:
		return render_template('prueba4.html', dato1=parm1, dato2=diccionario)
	elif parm1:
		return '<center><h4>Solo se tiene el parámetro {}</h4></center><br><p>Fin...</p>'.format(parm1)
	else:
		asteriscos = []
		for i in range(0, parm2):
			asteriscos.append('*')
		return 'Asteriscos: {}'.format(asteriscos)

if __name__ == '__main__':
	"""!
	Se ejecuta el servidor, el puerto por defecto es el 5000
	se usa debug en True para poder detectar los cambios realizados
	sobre el proyecto sin necesidad de ejecutar nuevamente el proyecto
	"""
	app.run(debug = True, port = 8080)