from servicios.aprobadosReprobadosDatos import getDataAprobadosReprobadosDashboard,getDataAprobadosReprobadosTabla
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return "Servidor funcionando de manera correcta"


@app.route('/aprob_reprob_dashboard', methods=['GET'])
def getDatashboard():
    return jsonify(getDataAprobadosReprobadosDashboard())


@app.route('/aprob_reprob_tabla', methods=['GET'])
def getDatasTabla():
    return jsonify(getDataAprobadosReprobadosTabla())


if __name__ == '__main__':
    app.run(debug=True, port=4000)