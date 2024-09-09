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
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos')
    data = cur.fetchall()
    return render_template('index.html', contactos = data)


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

@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos WHERE id = %s', [id])
    data = cur.fetchall()
    return render_template('edit-contact.html', contacto = data[0])

@app.route('/update/<id>', methods =['POST'])
def update_contact(id):
    if request.method == 'POST':
        nombreCompleto = request.form['nombreCompleto']
        telefono = request.form['telefono']
        correo = request.form['correo']
        cur = mysql.connection.cursor()
        cur .execute("""
            UPDATE contactos
            SET nombreCompleto = %s,
                correo = %s,
                telefono = %s
            WHERE id = %s
        """, (nombreCompleto, correo, telefono, id))
        mysql.connection.commit()
        flash('Contacto Actualizado Exitosamente')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contactos WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Removido Exitosamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)