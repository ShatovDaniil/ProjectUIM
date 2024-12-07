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
        inputData[col] = inputData[col].apply(lambda x: np.nan if pd.notna(x) and x > 100 else x)


   #ROZDELIM SPORTOVCE NA DVE SKUPINY PODLE PARAMETRU PTS(POCET BODU) PRO NASLEDUJICI ANALYZU

    # max_pts = 0
    # for value in inputData['pts']:
    #     if not pd.isna(value):
    #         if value > max_pts:
    #             max_pts = value
    # prah_rozdeleni = np.round(max_pts/2)
    #
    # index_sportovce_nad = []
    # index_sportovce_pod = []
    # for idx, value in enumerate(inputData['pts']):
    #     if pd.isna(value) or value <= prah_rozdeleni:
    #         index_sportovce_pod.append(idx)
    #     else:
    #         index_sportovce_nad.append(idx)
    #
    # group_nad = inputData.loc[index_sportovce_nad]
    # group_pod = inputData.loc[index_sportovce_pod]

    max_pts = inputData['pts'].max(skipna=True)
    prah_rozdeleni = np.round(max_pts / 2)

    index_sportovce_nad = inputData['pts'] > prah_rozdeleni
    index_sportovce_pod = ~index_sportovce_nad

    group_nad = inputData.loc[index_sportovce_nad].copy()
    group_pod = inputData.loc[index_sportovce_pod].copy()

    #BUDU HLEDAT CHYBEJICI HODNOTY A NAHRAZOVAT JE MEDIANEM VE SKUPINE

    # for column in group_nad.columns:
    #     median_value = group_nad[column].median()
    #     group_nad[column].fillna(median_value, inplace=True)
    #
    # inputData.loc[index_sportovce_nad] = group_nad
    #
    # for column_p in group_pod.columns:
    #     median_value = group_pod[column_p].median()
    #     group_pod[column_p].fillna(median_value, inplace=True)
    #
    #
    # inputData.loc[index_sportovce_pod] = group_pod
    #
    #
    #
    # preprocessedData = inputData.copy()
    numeric_columns = group_nad.select_dtypes(include=[np.number]).columns

    for column in numeric_columns:
        group_nad[column] = group_nad[column].fillna(group_nad[column].median())
        group_pod[column] = group_pod[column].fillna(group_pod[column].median())

    inputData.loc[group_nad.index, numeric_columns] = group_nad[numeric_columns]
    inputData.loc[group_pod.index, numeric_columns] = group_pod[numeric_columns]
    preprocessedData = inputData.copy()

    #MATICE KORELACE PRIZNAKU PTS S OSTATNIMY PRIZNAKY
    # correlation_matrix = preprocessedData.corr()
    # correlation_with_pts = correlation_matrix['pts']
    correlation_matrix = preprocessedData.select_dtypes(include=[np.number]).corr()
    correlation_with_pts = correlation_matrix['pts']  # ?????
    # output_path = "C:/Users/MagicBook/PycharmProjects/pythonProject/ProjectUIM/PreprocessedNBAData.csv"
    # if output_path:
    #     preprocessedData.to_csv(output_path, index=False)

    return preprocessedData

