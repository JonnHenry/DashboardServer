import os
import json

dir = os.path.dirname(__file__)
urlData = os.path.abspath(os.path.join(dir,'../data/DatosEstadisticos.json'))

try:
    with open(urlData) as file:
        data = json.load(file)
except:
    data = {}

def getDataAprobReprobados():
    return data
