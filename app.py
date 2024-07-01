from flask import Flask,redirect,url_for,render_template,request
from flask_mysqldb import MySQL
from datetime import datetime
import os

app=Flask(__name__)


app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "stock_cac2024"
mysql = MySQL(app)

CARPETA = os.path.join('uploads')
app.config['CARPETA'] = CARPETA

@app.route('/')
def index():
    return render_template('productos/index.html')

@app.route('/contacto')
def contacto():
    return render_template('/contacto.html')

@app.route('/experencias')
def experiencias():
    return render_template('/experiencias.html')

@app.route('/productos')
def productos():
    return render_template('/productos.html')

@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/admin', methods=['POST'])
def admin():
    usuario = request.form['user']
    pwd = request.form['password']
    
    if usuario == 'admin' and pwd == 'admin':
        return render_template('productos/admin.html')
    else:
        return render_template('/login.html')
        
@app.route('/stock')
def stock():
    sql = "SELECT * FROM stock_cac2024.productos;"
    
    conn = mysql.connection.cursor()
    conn.execute(sql)
    productos = conn.fetchall()
    return render_template('productos/stock.html', productos=productos)

@app.route('/alta')
def alta():
    return render_template('productos/alta.html')

@app.route('/crear', methods=['POST'])
def crear():
    _nombre = request.form['nombre']
    _categoria = request.form['categoria']
    _precio = request.form['precio']
    _cantidad = request.form['cantidad']
    _foto = request.files['foto']
    
    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S%f")
    
    if _foto.filename != '':
        nNomFoto = tiempo + _foto.filename
        _foto.save("uploads/"+nNomFoto)
    
    
    sql ="INSERT INTO `productos` (`id`, `nombre`, `categoria`, `precio`, `cantidad`, `imagen`) VALUES (NULL, %s, %s, %s, %s, %s);"
    datos = (_nombre, _categoria, _precio, _cantidad, nNomFoto)
    
    conn = mysql.connection.cursor()
    conn.execute(sql,datos)
    mysql.connection.commit()
    return render_template('productos/alta.html')

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = mysql.connection.cursor()
    
    conn.execute("SELECT imagen FROM stock_cac2024.productos WHERE id=%s", (id,))
    fila = conn.fetchall()
    os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
    
    conn.execute("DELETE FROM stock_cac2024.productos WHERE id=%s", (id,))
    mysql.connection.commit()
    return redirect('/stock')

@app.route('/editar/<int:id>')
def editar(id):
      
    conn = mysql.connection.cursor()
    conn.execute("SELECT * FROM stock_cac2024.productos WHERE id=%s;", (id,))
    productos = conn.fetchall()
    mysql.connection.commit()
    
    return render_template('productos/edit.html', productos=productos)

@app.route('/update', methods=['POST'])
def update():
    _id = request.form['idproducto']
    _nombre = request.form['nombre']
    _categoria = request.form['categoria']
    _precio = request.form['precio']
    _cantidad = request.form['cantidad']
    _foto = request.files['foto']
        
    
    
    conn = mysql.connection.cursor()
    
    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S%f")
    
    if _foto.filename != '':
        nNomFoto = tiempo + _foto.filename
        _foto.save("uploads/"+nNomFoto)
        conn.execute("SELECT imagen FROM stock_cac2024.productos WHERE id=%s", (_id,))
        fila = conn.fetchall()
        os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
        conn.execute("UPDATE stock_cac2024.productos SET `imagen`=%s WHERE id=%s;", (nNomFoto, (_id,)))
        mysql.connection.commit()
        
    sql = "UPDATE stock_cac2024.productos SET `nombre`=%s,`categoria`=%s,`precio`=%s,`cantidad`=%s,`imagen`=%s WHERE id=%s;"
    datos = (_nombre, _categoria, _precio, _cantidad, nNomFoto, _id)
        
    conn.execute(sql, datos)
    mysql.connection.commit()
    return redirect('/stock')
    
    

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)