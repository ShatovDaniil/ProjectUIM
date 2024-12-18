# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:03:17 2022

@author: xredin00
"""
import numpy as np
from joblib import load

def MyModel(data):
#     Funkce slouzi k implementaci nauceneho modelu. Vas model bude ulozen v samostatne promenne a se spustenim se aplikuje
#     na vstupni data. Tedy, model se nebude pri kazdem spousteni znovu ucit. Ostatni kod, kterym doslo k nauceni modelu,
#     take odevzdejte v ramci projektu.

#Vstup:             data:           vstupni surova data reprezentujici 1
#                                   objekt (1 pacienta, 1 obrazek, 1 casovou radu, apod.). 

#Vystup:            output:         zarazeni objektu do tridy


    model_filename = r"C:\Users\MagicBook\PycharmProjects\pythonProject\ProjectUIM\trained_model.joblib"

    model = load(model_filename)
    output = model.predict(data)


    return output