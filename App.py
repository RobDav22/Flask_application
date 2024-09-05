from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexion a base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']= 'password'
app.config['MYSQL_DB'] = 'flaskCRUD'
mysql = MySQL(app)

# Configuraciones
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nombreCompleto = request.form['nombreCompleto']
        telefono = request.form['telefono']
        correo = request.form['correo']
        print(nombreCompleto)
        print(telefono)
        print(correo)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contactos (nombreCompleto, telefono, correo) VALUES (%s, %s, %s)', 
        (nombreCompleto, telefono, correo))
        mysql.connection.commit()
        flash('Contacto Agregado Exitosamente')
        return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
    return 'Editar contacto'

@app.route('/delete')
def delete_contact():
    return 'Eliminar contacto'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)