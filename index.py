from flask import Flask, render_template

app = Flask(__name__)
"""
@app.route('/') #Aqui estamos definiendo la ruta raiz
def principal(): #Aquí estamos defniiendo un métodp, el cual retornará el siguiente mensaje
    #return "Bienvenidoo bienvenida a mi sitio web con python" 
    return "BIenvenido a mi página nueva"
@app.route('/contacto')
def contacto():
    return "Esta es la pagina de contacto"


if __name__ == '__main__':
    app.run(debug=True, port=5017)#El debug=true le indica a mi servidor que aun estamos haciendo cambios, y que por cada cambio hará una actualización el servidor
"""

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/lenguajes')
def mostrarlenguajes():
    mislenguajes=("PHP","Python","Java","C#","JavaScript","Perl","Ruby","Rust")
    return render_template('lenguajes.html',lenguajes=mislenguajes)#El lenguajes es el nombre que le estamos asignando al grupo que le enviaresmo al lenguajes .html, y mislenguajes es una tupla que estamos llamadno#

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True, port=5017)