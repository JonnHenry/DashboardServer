from servicios.aprobadosReprobadosDatos import getDataAprobReprobados
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return "Servidor funcionando de manera correcta"


@app.route('/aprob_reprob', methods=['GET'])
def getProducts():
    return jsonify(getDataAprobReprobados())



if __name__ == '__main__':
    app.run(debug=True, port=4000)