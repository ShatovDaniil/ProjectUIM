# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:52:48 2022

@author: rredi
"""
import os



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


