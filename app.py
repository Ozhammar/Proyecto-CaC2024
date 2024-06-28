from flask import Flask,redirect,url_for,render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)


app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "stock_cac2024"
mysql = MySQL(app)

# sql ="INSERT INTO `productos` (`id`, `nombre`, `categoria`, `precio`, `imagen`, `caraceristicas`) VALUES (NULL, '', '', '', '', '');"
# conn = mysql.connect()
# cursor = conn.cursor()
# cursor.execute(sql)
# conn.commit()



@app.route('/')
def index():
    sql ="INSERT INTO `productos` (`nombre`, `categoria`, `precio`, `imagen`, `caraceristicas`) VALUES ('i7', 'microprocesador', '50000', '', 'microprocesador intel caro');"
    conn = mysql.connection.cursor()
    conn.execute(sql)
    mysql.connection.commit()
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
        



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)