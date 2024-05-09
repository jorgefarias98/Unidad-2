from flask import Flask, render_template, request
from analizador_lexico import analizar_lexico
from analizador_sintactico import analizar_codigo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', resultado_lexico='', resultado_sintactico='')

@app.route('/analizar', methods=['POST'])
def analizar():
    global cont
    codigo = request.form['codigo']
    cont = 1  # Reiniciar el número de línea
    resultado = analizar_lexico(codigo)
    resultadoParser=analizar_codigo(codigo)
    return render_template('index.html', codigo=codigo, resultado1=resultado, resultadoParser=resultadoParser)

if __name__ == '__main__':
    app.run(debug=True)