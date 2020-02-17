#import numpy as np
import pickle
import pandas as pd
from warnings import simplefilter
import os

dir = os.path.dirname(__file__)
simplefilter(action='ignore', category=FutureWarning)

def prediccionRegresionLineal(dfNewPrediccion):
    #Modelo de regresion lineal
    urlRegresionLineal = os.path.abspath(os.path.join(dir,'../data/modelo_regresion_logistica.sav'))
    regresion_logistica = pickle.load(open(urlRegresionLineal, 'rb'))
    return regresion_logistica.predict(dfNewPrediccion)

def prediccionForestClassifier(dfNewPrediccion):
    #Modelo Forest Classifier
    urlForestClassifier = os.path.abspath(os.path.join(dir,'../data/modelo_random_forest_classifier.sav'))
    random_forest_classifier = pickle.load(open(urlForestClassifier, 'rb'))
    return random_forest_classifier.predict(dfNewPrediccion)

def prediccionVectorMachine(dfNewPrediccion):
    #Modelo Vector Machine
    urlVectorMachine = os.path.abspath(os.path.join(dir,'../data/modelo_support_vector_machine.sav'))
    support_vector_machine = pickle.load(open(urlVectorMachine, 'rb'))
    return support_vector_machine.predict(dfNewPrediccion)

def prediccionClasificacion(prmdDurcinSes,prmdDurcinSesVideoLecturas,prmdDurcinSesEvaluacionSumativas, prmdDurcinSesEvaluacionFormativas):
    diccionarioResultados = dict()
    dfPrediccion = pd.DataFrame({'promedio_duracion_sesione': [prmdDurcinSes], 'promedio_video_lecturas_sesiones': [prmdDurcinSesVideoLecturas], 'promedio_evaluaciones_sumativas_sesiones': [prmdDurcinSesEvaluacionSumativas], 'promedio_evaluaciones_formativas_sesiones': [prmdDurcinSesEvaluacionFormativas]})
    diccionarioResultados['regresionLineal'] = prediccionRegresionLineal(dfPrediccion)[0]
    diccionarioResultados['forestClassifier'] = prediccionForestClassifier(dfPrediccion)[0]
    diccionarioResultados['vectorMachine'] = prediccionVectorMachine(dfPrediccion)[0]
    return diccionarioResultados

