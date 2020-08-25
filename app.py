from flask import Flask, flash, render_template, redirect, request, url_for
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename

# Set the app flask
app = Flask(__name__)


# Set the config for the database
app.config['MYSQL_USER'] = 'sql10361967'
app.config['MYSQL_PASSWORD'] = 'ALDEb45sxH'
app.config['MYSQL_HOST'] = 'sql10.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql10361967'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# set the secret key
app.secret_key = 'MySecretKey'


# Set the database on the app
mysql = MySQL(app)


# Route for landing page
@app.route('/')
def index():
    return render_template('index.html')


# Route for Client
@app.route('/client')
def client():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from clientes''')
    sql_cli = cur.fetchall()
    return render_template('client.html', cliente=sql_cli)


# Route for add client
@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        foto = request.files['foto']
        foto_name = secure_filename(foto.filename)
        foto.save('/home/jaarmore/test-tsakana/static/user_files/' + foto_name)
        print(cedula, nombre, direccion, telefono, foto_name)

        # Insert data into database
        cur = mysql.connection.cursor()
        cur.execute('''
              INSERT INTO clientes(cedula, nombre, direccion, telefono, foto)
              VALUES (%s, %s, %s, %s, %s)
              ''', (cedula, nombre, direccion, telefono, foto_name))
        mysql.connection.commit()
        flash('Cliente agregado con exito')
        return redirect(url_for('client'))
    else:
        return render_template('client.html')


# Route for edit client
@app.route('/edit_client/<string:id>')
def edit_client(id):
    cur = mysql.connection.cursor()
    cur.execute('''
      SELECT * FROM clientes WHERE id = {}
    '''.format(id))
    client = cur.fetchall()
    return render_template('update_client.html', data=client[0])


@app.route('/update_client/<string:id>', methods=['POST'])
def update_client(id):
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        foto = request.files['foto']
        foto_name = secure_filename(foto.filename)
        foto.save('/home/jaarmore/test-tsakana/static/user_files/' + foto_name)
        print(cedula, nombre, direccion, telefono, foto_name)
        cur = mysql.connection.cursor()
        cur.execute('''
          UPDATE clientes
          SET
            cedula = %s,
            nombre = %s,
            direccion = %s,
            telefono = %s,
            foto = %s
          WHERE id = %s
        ''', (cedula, nombre, direccion, telefono, foto_name, id))
        mysql.connection.commit()
        flash('Cliente Actualizado!')
        return redirect(url_for('client'))


# Route for delete client
@app.route('/delete_client/<string:id>')
def delete_client(id):
    cur = mysql.connection.cursor()
    cur.execute('''
      DELETE FROM clientes WHERE id = {}
    '''.format(id))
    mysql.connection.commit()
    flash('Cliente removido!')
    return redirect(url_for('client'))


# Route for Product
@app.route('/product')
def product():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from productos''')
    sql_cli = cur.fetchall()
    return render_template('product.html', product=sql_cli)


# Route for add product
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        codigo = request.form['codigo']
        categoria = request.form['categoria']
        nombre = request.form['nombreprod']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        estado = request.form['estado']
        print(codigo, categoria, nombre, precio, cantidad)

        # Insert data into database
        cur = mysql.connection.cursor()
        cur.execute('''
          INSERT
          INTO productos(codigo, categoria, nomprod, precio, cantbod, estado)
          VALUES (%s, %s, %s, %s, %s, %s)
        ''', (codigo, categoria, nombre, precio, cantidad, estado))
        mysql.connection.commit()
        flash('Producto agregado con exito')
        return redirect(url_for('product'))
    else:
        return render_template('product.html')


# call to flask app
if __name__ == '__main__':
    app.run(debug=True)
