from flask import Flask,redirect,url_for,render_template,request,send_from_directory,session
from flask_mysqldb import MySQL
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import random
import os


app=Flask(__name__)
app.secret_key = 'your_secret_key'

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "stock_cac2024"


mysql = MySQL(app)


CARPETA = os.path.join('uploads')
app.config['CARPETA'] = CARPETA

@app.route('/')
def index():
    sql = "SELECT id FROM `productos`;"
    conn = mysql.connection.cursor()
    conn.execute(sql)
    ids = conn.fetchall()
    ids_carry = list(tuple(random.randint(ids[0][0], ids[-1][-1]) for _ in range(9)))
    conn.execute("SELECT * FROM productos WHERE id IN %s", (ids_carry,))
    productos = conn.fetchall()
    conn.close()
       
    
    return render_template('productos/index.html', productos=productos)

@app.route('/contacto')
def contacto():
    return render_template('/contacto.html')

@app.route('/experencias')
def experiencias():
    return render_template('/experiencias.html')

@app.route('/productos', methods=['GET'])
def productos():
    try:
        categoria = request.args.get('categoria')
        conn = mysql.connection.cursor()
        if categoria:
            sql = "SELECT * FROM productos WHERE categoria = %s"
            conn.execute(sql, (categoria,))
        else:
            sql = "SELECT * FROM productos"
            conn.execute(sql)
        productos = conn.fetchall()
        conn.close()
        return render_template('productos.html', productos=productos)
    
    except mysql.connector.Error as e:
        return f"Error de base de datos: {e}", 500
    except Exception as e:
        return str(e), 500

@app.route('/login')
def login():
    return render_template('/login.html')

def dataFromdb():
    sql= "SELECT `categoria`, SUM(`cantidad`) as total_cantidad FROM `productos` GROUP BY `categoria`"
    conn = mysql.connection.cursor()
    conn.execute(sql)
    resultado = conn.fetchall()
    categorias = [row[0] for row in resultado]
    cantidades = [row[1] for row in resultado]
    conn.close()
    return categorias, cantidades

@app.route('/admin', methods=['POST'])
def admin():
    usuario = request.form['user']
    pwd = request.form['password']
    
    categorias, cantidades = dataFromdb()
    plt.figure(figsize=(15, 5))
    colors = plt.cm.tab20(np.linspace(0, 1, len(categorias)))
    plt.barh(categorias, cantidades, color=colors)
    plt.title('Stock por Categoria')
    plt.xlabel('Cantidad')
    image_path = 'uploads/bar_chart.png'
    plt.savefig(image_path)
    plt.close()
    
    if usuario == 'admin' and pwd == 'admin':
        return render_template('productos/admin.html', image_path=image_path)
    else:
        return render_template('/login.html')
    
@app.route('/registro.html', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password = request.form['password']
        password_conf = request.form['password_conf']
    
    
    
        conn = mysql.connection.cursor()

        conn.execute("SELECT * FROM usuario WHERE usuario =%s",(usuario,))
        existing_user = conn.fetchone()
        
    
        conn.execute(
            "INSERT INTO usuario (usuario, nombre, apellido, email, password, password_conf) VALUES (%s,%s, %s, %s, %s, %s)",
                (usuario, nombre, apellido, email, password, password_conf)
        )
        mysql.connection.commit()
        conn.close()

        return redirect(url_for('login'))
    return render_template('productos/registro.html')



@app.route('/stock')
def stock():
    sql = "SELECT * FROM stock_cac2024.productos;"
    
    conn = mysql.connection.cursor()
    conn.execute(sql)
    productos = conn.fetchall()
    conn.close()
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
    conn.close()
    return render_template('productos/alta.html')

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = mysql.connection.cursor()
    
    conn.execute("SELECT imagen FROM stock_cac2024.productos WHERE id=%s", (id,))
    fila = conn.fetchall()
    os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
    
    conn.execute("DELETE FROM stock_cac2024.productos WHERE id=%s", (id,))
    mysql.connection.commit()
    conn.close()
    return redirect('/stock')

@app.route('/editar/<int:id>')
def editar(id):
      
    conn = mysql.connection.cursor()
    conn.execute("SELECT * FROM stock_cac2024.productos WHERE id=%s;", (id,))
    productos = conn.fetchall()
    mysql.connection.commit()
    conn.close()
    print(productos)
    
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
    
    conn.execute("SELECT imagen FROM stock_cac2024.productos WHERE id=%s", (_id,))
    nombrefetch=conn.fetchall()
    nNomFoto = nombrefetch[0]
    print(nNomFoto)
    
    
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
    conn.close()
    return redirect('/stock')

@app.route('/uploads/<nombreImagen>')
def uploads(nombreImagen):
    return send_from_directory(app.config['CARPETA'], nombreImagen)
    
    

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)