from flask import Flask

# Se crea un nuevo objeto
app = Flask(__name__)

"""!
Wrap o decorador, se especifica la ruta en la que se va a 
ejecutar la función index
Ruta raiz
"""
@app.route('/')
# Se crea una función a ejecutar sobre la url
def index():
	# Regresa un string en el explorador
	return 'Página raiz'

# Ruta opcional
@app.route('/hijo_1')
@app.route('/hijo_1/<parm1>')
@app.route('/hijo_1/<parm1>/<int:parm2>')
def prueba1(parm1 = None, parm2 = None):
	"""!
	Se crea una función a ejecutar sobre la url
	parm1: es un parámetro pasado con la url
	"""

	# Uso de uno de los parámetros para seleccionar lo que se muestra en el explorador
	if parm1 and parm2:
		if parm2 > 18:
			return 'Bienvenido {}'.format(parm1)
		else:
			return 'Se ha ingresado el parámetro {}'.format(parm1)
	else:
		return 'No se tienen los dos parámetros'

"""!
Se ejecuta el servidor, el puerto por defecto es el 5000
se usa debug en True para poder detectar los cambios realizados
sobre el proyecto sin necesidad de ejecutar nuevamente el proyecto
"""
if __name__ == '__main__':
	app.run(debug = True, port = 8080)