from flask import Flask, request
from model import model
app = Flask(__name__)

@app.route('/procesar_datos', methods=['POST'])
def procesar_datos():
    datos = request.form
    edad = int(datos['edad'])
    sexo = datos['sexo']
    
    modelo = model()
    # Procesar los datos y devolver la información deseada
    return model.predecir(datos)

if __name__ == '__main__':
    app.run()