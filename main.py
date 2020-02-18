from servicios.aprobadosReprobadosDatos import getDataAprobadosReprobadosDashboard,getDataAprobadosReprobadosTabla
from servicios.prediccionClasificacion import prediccionClasificacion

from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
app.config['TESTING'] = True


@app.route('/', methods=['GET'])
def ping():
    return "Servidor funcionando de manera correcta"


@app.route('/aprob_reprob_dashboard', methods=['GET'])
def getDatashboard():
    return jsonify(getDataAprobadosReprobadosDashboard())


@app.route('/aprob_reprob_tabla', methods=['GET'])
def getDatasTabla():
    return jsonify(getDataAprobadosReprobadosTabla())


#prmdDurcinSes,prmdDurcinSesVideoLecturas,prmdDurcinSesEvaluacionSumativas, prmdDurcinSesEvaluacionFormativas
@app.route('/prediccion', methods=['POST'])
def prediccion():
    prmdDurcinSes = request.json['prmdDurcinSes']
    prmdDurcinSesVideoLecturas = request.json['prmdDurcinSesVideoLecturas']
    prmdDurcinSesEvaluacionSumativas = request.json['prmdDurcinSesEvaluacionSumativas']
    prmdDurcinSesEvaluacionFormativas = request.json['prmdDurcinSesEvaluacionFormativas']
    try:
        resultadosPrediccion = prediccionClasificacion(prmdDurcinSes,prmdDurcinSesVideoLecturas,prmdDurcinSesEvaluacionSumativas,prmdDurcinSesEvaluacionFormativas)
        response = jsonify({
            'regresionLineal': apruebaReprueba(resultadosPrediccion.get('regresionLineal')),
            'forestClassifier': apruebaReprueba(resultadosPrediccion.get('forestClassifier')),
            'vectorMachine': apruebaReprueba(resultadosPrediccion.get('vectorMachine')),
            'error': False,
            'aprueba': resultadoGeneral(resultadosPrediccion)
        })
        return response
    except:
        responseError = jsonify({
            'regresionLineal': 'Reprueba',
            'forestClassifier': 'Reprueba',
            'vectorMachine': 'Reprueba',
            'error': True,
            'aprueba': False
        })
        return responseError
        
def apruebaReprueba(valor):
    if valor==1:
        return 'Aprueba'
    else:
        return 'Reprueba'


def resultadoGeneral(dicResult):
    resultado = dicResult.get('regresionLineal')+dicResult.get('forestClassifier')+dicResult.get('vectorMachine')
    #aprueba
    if resultado>1:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(debug=True,port=8080)


    