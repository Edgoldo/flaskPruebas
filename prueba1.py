from flask import Flask
from flask import request

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
# Se crea una función a ejecutar sobre la url
def prueba1():
	# Regresa un string en el explorador
	return 'Enlace a primer hijo'

# Ruta opcional 2 con parámetros
@app.route('/hijo_2')
# Se crea una función a ejecutar sobre la url
def prueba2():
	# Obtiene los parámetros entrantes por la url a través de: ?param1=valor
	par1 = request.args.get('parm1', 'Vacio')
	# ?param2=valor
	par2 = request.args.get('parm2', 'Parámetro 2')
	# Regresa un string en el explorador
	return 'Valor del primer parámetro: {} y el segundo {}'.format(par1, par2)
"""!
Se ejecuta el servidor, el puerto por defecto es el 5000
se usa debug en True para poder detectar los cambios realizados
sobre el proyecto sin necesidad de ejecutar nuevamente el proyecto
"""
if __name__ == '__main__':
	app.run(debug = True, port = 8080)