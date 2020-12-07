
from flask import Flask, render_template, request, redirect, url_for
from db import Epoca,app,MatrizQ,db
#app = Flask (__name__)


# se crea la base de datos, se carga la interfaz del servidor. Al final, se vuelve a la pagina principal del servidor

@app.route("/") 
def index():
	db.create_all()  					
	E=Epoca.query.all()
	# Q=MatrizQ.query.all()
	obj = MatrizQ.query.all () 
	Q =(obj[-1])

	return render_template("index.html", Q = Q)


# se exporta los valores de la matriz Q a un excel. Al final, se vuelve a la pagina principal del servidor

@app.route("/exportar")
def exp():
	import os
	# Q=MatrizQ.query.all()
	
	os.system('python exportarExcel.py')
	return redirect(url_for('index'))


# se ejecuta el codigo caminar.py el cual hace caminar al robot con la matriz q aprendida. Al final, se vuelve a la pagina principal del servidor

@app.route("/caminar")
def cam():
	import os
	os.system('python ./PythonCode/Demo/Caminar.py')
	return redirect(url_for('index'))

# se ejecuta el codigo RunQ.py para que el robot aprenda cuales son los valores necesarios apra caminar y al final, se vuelve a la pagina principal del servidor

@app.route("/aprender")
def aprender():
	import os
	os.system('python ./PythonCode/Demo/RunQ.py')
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)
