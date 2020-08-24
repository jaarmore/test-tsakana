from flask import Flask, render_template, request, url_for
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


# Set the database on the app
mysql = MySQL(app)


# Route for landing page
@app.route('/')
def index():
    return render_template('index.html')


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
        return 'Data saved!'
    else:
        return render_template('client.html')


# Route for edit client
@app.route('/edit_client')
def edit_client():
    return 'Client edited'


# Route for delete client
@app.route('/delete_client')
def delete_client():
    return 'Client deleted'


# call to flask app
if __name__ == '__main__':
    app.run(debug=True)
