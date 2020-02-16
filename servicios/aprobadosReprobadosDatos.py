import os

dir = os.path.dirname(__file__)

#Para el dashboard de los graficos
urlDataDashbard = os.path.abspath(os.path.join(dir,'../data/aprobadosReprobadosDashboard.json'))
try:
    with open(urlDataDashbard) as file:
        dataDashboard = json.load(file)
except:
    dataDashboard = {}

def getDataAprobadosReprobadosDashboard():
    return dataDashboard



#Para las tablas del dashboard
urlDataTable = os.path.abspath(os.path.join(dir,'../data/aprobadosReprobadosTabla.json'))
try:
    with open(urlDataTable) as file:
        dataTabla = json.load(file)
except:
    dataTabla = {}


def getDataAprobadosReprobadosTabla():
    return dataTabla
