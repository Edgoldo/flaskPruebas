from flask import Flask

# Se crea un nuevo objeto
app = Flask(__name__)

"""!
Wrap o decorador, se especifica la ruta en la que se va a 
ejecutar la función index
"""
@app.route('/')
# Se crea una función a ejecutar sobre la url
def index():
	# Regresa un string en el explorador
	return '<b>Hola mundo</b></br>'
"""!
Se ejecuta el servidor, el puerto por defecto es el 5000
se usa debug en True para poder detectar los cambios realizados
sobre el proyecto sin necesidad de ejecutar nuevamente el proyecto
"""
app.run(debug = True, port = 8080)