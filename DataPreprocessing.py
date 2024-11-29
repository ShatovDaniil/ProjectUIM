# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:52:48 2022

@author: rredi
"""
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def DataPreprocessing(inputData):
    """
    Funkce slouzi pro predzpracovani dat, ktera slouzi k testovani modelu. Veskery kod, ktery vedl k nastaveni
    jednotlivych kroku predzpracovani (vcetne vypoctu konstant, prumeru, smerodatnych odchylek, atp.) budou odevzdany
    spolu s celym projektem.

    :parameter inputData:
        Vstupni data, ktera se budou predzpracovavat.
    :return preprocessedData:
        Predzpracovana data na vystup
    """

    try:
        base, ext = os.path.splitext(inputData)
        output_file = f"{base}_cleaned{ext}"

        with open(inputData, "r", encoding="utf-8") as file:
            lines = file.readlines()
            clean_lines = []

            for line in lines:
                if "NaN" not in line:
                    clean_lines.append(line)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(clean_lines)
        return output_file


    except:
        print("Ne")
        return None

path = "C:/Users/Daniil/PycharmProjects/pythonProject/UIMprojekt/TrainNBAData.csv"
DataPreprocessing(path)

def VizPairplot(preprocessedData):
    cols = ['gp', 'min', 'pts', 'fg', 'ft']

    new_column_names = {
        'gp': 'Počet zápasů',
        'min': 'Počet minut',
        'pts': 'Počet bodů ',
        'fg': 'Střelecké pokusy(%)',
        'ft': 'Trestné hody(%)',
    }

    df_renamed = preprocessedData[cols].rename(columns=new_column_names)

    sns.pairplot(df_renamed)
    plt.show()



def Vizhist(preprocessedData:object,
            name_column:str):
    plt.figure(figsize= (14,5))
    sns.histplot(preprocessedData[name_column],kde = True)
    plt.show()

def VizBoxplot(preprocessedData:object,
            name_column:str):
    plt.figure(figsize=(20,12))
    sns.boxplot(x=preprocessedData[name_column])

    plt.show()


