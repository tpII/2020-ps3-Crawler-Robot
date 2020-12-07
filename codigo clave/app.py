
from flask import Flask, render_template, request, redirect, url_for
from db import Epoca,app,MatrizQ,db
#app = Flask (__name__)

@app.route("/") 
def index():
	db.create_all()
	E=Epoca.query.all()
	# Q=MatrizQ.query.all()
	obj = MatrizQ.query.all () 
	Q =(obj[-1])

	return render_template("index.html", Q = Q)

@app.route("/exportar")
def exp():
	import os
	# Q=MatrizQ.query.all()
	
	os.system('python exportarExcel.py')
	return redirect(url_for('index'))

@app.route("/caminar")
def cam():
	import os
	os.system('python ./PythonCode/Demo/Caminar.py')
	return redirect(url_for('index'))


@app.route("/aprender")
def aprender():
	import os
	os.system('python ./PythonCode/Demo/RunQ.py')
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)