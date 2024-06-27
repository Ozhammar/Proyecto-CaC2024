from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

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



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)