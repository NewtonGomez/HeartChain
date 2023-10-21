from flask import Flask, request
from model import model
app = Flask(__name__)
modelo = model() # entrena en segundo plano

@app.route('/procesar_datos', methods=['POST'])
def procesar_datos():
    datos = request.form
    edad = int(datos['edad'])
    sexo = datos['sexo']
    data = datos['datos']
    
    # Procesar los datos y devolver la información deseada
    return model.predecir(data)

if __name__ == '__main__':
    app.run()