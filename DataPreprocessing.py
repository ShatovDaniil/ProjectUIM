# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:52:48 2022

@author: rredi
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def DataPreprocessing(inputData):

    #ZBAVIM SE MOZNYCH ANOMALNICH HODNOT VE SLOUPCICH FG Střelecké pokusy (%)', 'x3P Tříbodové hody (%)', 'FT Trestné hody (%), KDE MAXIMUM JE 100%
    #HODNOTY >100% NAHRADIM NaN, O PAR KROKU POZDEJI BUDU JE NAHRAZOVAT MEDIANEM VE SLOUPCI VE SKUPINE
    columns_to_check = ['fg', 'x3p', 'ft']
    for col in columns_to_check:
        inputData[col] = inputData[col].apply(lambda x: np.nan if x > 100 else x)


   #ROZDELIM SPORTOVCE NA DVE SKUPINY PODLE PARAMETRU PTS(POCET BODU) PRO NASLEDUJICI ANALYZU

    max_pts = 0
    for value in inputData['pts']:
        if not pd.isna(value):
            if value > max_pts:
                max_pts = value
    prah_rozdeleni = np.round(max_pts/2)

    index_sportovce_nad = []
    index_sportovce_pod = []
    for idx, value in enumerate(inputData['pts']):
        if pd.isna(value) or value <= prah_rozdeleni:
            index_sportovce_pod.append(idx)
        else:
            index_sportovce_nad.append(idx)

    group_nad = inputData.loc[index_sportovce_nad]
    group_pod = inputData.loc[index_sportovce_pod]

    #BUDU HLEDAT CHYBEJICI HODNOTY A NAHRAZOVAT JE MEDIANEM VE SKUPINE

    for column in group_nad.columns:
        median_value = group_nad[column].median()
        group_nad[column].fillna(median_value, inplace=True)

    inputData.loc[index_sportovce_nad] = group_nad

    for column_p in group_pod.columns:
        median_value = group_pod[column_p].median()
        group_pod[column_p].fillna(median_value, inplace=True)


    inputData.loc[index_sportovce_pod] = group_pod



    preprocessedData = inputData.copy()

    #MATICE KORELACE PRIZNAKU PTS S OSTATNIMY PRIZNAKY
    correlation_matrix = preprocessedData.corr()
    correlation_with_pts = correlation_matrix['pts']


    print("РАЗМЕР НА ВЫХОДЕ ИЗ ПРЕДОБРАБОТКИ:", preprocessedData.shape)

    return preprocessedData
path = "C:/Users/Daniil/PycharmProjects/pythonProject/UIMprojekt/TrainNBAData.csv"
DataPreprocessing(path)

