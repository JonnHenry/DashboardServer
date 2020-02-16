import pandas as pd
from flask import Flask, jsonify, request
import os
import copy

import json

dir = os.path.dirname(__file__)


urlAprobados = os.path.abspath(os.path.join(dir,'../dataset/DatosEstadisticos.json'))

