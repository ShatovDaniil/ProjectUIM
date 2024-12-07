# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:21:22 2022

@author: xredin00
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from DataPreprocessing import DataPreprocessing
from MyModel import MyModel
from GetScoreCareer import GetScoreCareer


def Main(filePath):
    
    # Funkce slouzi pro overeni klasifikacnich schopnosti navrzeneho modelu.
    # Model bude overovan na skryte mnozine dat, v odevzdanem projektu je proto
    # nutne dodrzet sktrukturu tohoto kodu. 
    
    # ======================= POZOR ==========================================
    # Odevzdany model se jiz NEBUDE ucit. Naucite jej vy, odevzdate a my ho
    # pri testovani jiz budeme POUZE volat a overovat jeho funkcnost.
    # ========================================================================
    
    # Vstup:     filePath:           Nazev slozky (textovy retezec) obsahujici data
    
    # Vystup:    se:                 Vysledna senzitivita modelu
    #            sp:                 Vysledna specificita modelu
    #            acc:                Vysledna presnost modelu
    #            fScore:             Vysledne F1 skore modelu
    #            ppv:                Pozitivni prediktivni hodnota
    #            confusionMatrix:    Matice zamen
    
    # Funkce:
    #            DataPreprocessing:  Funkce pro predzpracovani dat
    
    #            MyModel:            Funkce pro implementaci modelu. Nauceny model se bude nacitat z externiho souboru,
    #            nebude se ucit pri kazdem spusteni kodu. Veskery kod, ktery vedl k nauceni modelu,
    #            vsak bude soucasti odevzdaneho projektu. Do funkce vstupuje vzdy jen 1 objekt (sportovec, casova rada, pacient, obrazek, apod.)
    
    #            GetScoreCareer:     Funkce pro vyhodnoceni uspesnosti
    #            modelu. Z dostupnych hodnot vyberte do prezentace metriku
    #            vhodnou pro vase data (funkci neupravujte).    


    if os.path.isdir(filePath)==False:
        print("Wrong directory")
     #%% 1 - Nacteni dat
    inputData = pd.read_csv(f"{filePath}\\TrainNBAData.csv")
    numRecords = inputData.shape[0]
    confMatrix = np.zeros((2,2))
    #inputData['target_5yrs'] = inputData['target_5yrs'].map({'yes': 1, 'no': 0})

    for idx in range(numRecords):
        targetClass = inputData.target_5yrs[idx]
        if targetClass=='no':
            targetClass = 0
        else:
            targetClass = 1
            
        #%% 2 - Predzpracovani dat
        preprocessedData = DataPreprocessing(inputData) # Do zpracovani vstupuji vsechny informace o hraci (krome poradoveho cisla,jmena,score)

        #%% 3 - Vybaveni natrenovaneho modelu
        outputClass = MyModel(preprocessedData.drop(columns=['target_5yrs', 'Var1', 'name']))
        #plt.imshow()
        
        if outputClass.size == 1 and (outputClass == 0 or outputClass == 1):
            confMatrix[outputClass,targetClass] += 1
        else:
             print('Invalid class number. Operation aborted.')   
    se,sp,acc,ppv,fScore = GetScoreCareer(confMatrix)
    print(f"Sensitivity (Se): {se:.2f}")
    print(f"Specificity (Sp): {sp:.2f}")
    print(f"Accuracy (Acc): {acc:.2f}")
    print(f"Positive Predictive Value (PPV): {ppv:.2f}")
    print(f"F1 Score (FScore): {fScore:.2f}")
        
    return se,sp,acc,ppv,fScore, confMatrix


#se,sp,acc,ppv,fScore, confMatrix = Main('C:\\Users\\79028\\Documents\\UNI\\VUT\\PROJEKT UIM')

#se,sp,acc,ppv,fScore, confMatrix = Main('C:\\Users\\79028\\Documents\\UNI\\VUT\\PROJEKT UIM')
if __name__ == "__main__":
    filePath = "C:\\Users\\MagicBook\\PycharmProjects\\pythonProject\\ProjectUIM"
    se, sp, acc, ppv, fScore, confMatrix = Main(filePath)
