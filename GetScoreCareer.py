# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:43:14 2022

@author: xredin00
"""
import numpy as np
def GetScoreCareer(confMatrix):
    
    # Funkce pro vyhodnocení úspìšnosti modelu

    # Vstup:     confusionMatrix:    Matice zámìn z funkce Main()
    
    # Výstup:    se:                 Výsledná senzitivita modelu
    #            sp:                 Výsledná specificita modelu
    #            acc:                Výsledná pøesnost modelu
    #            fScore:             Výsledné F1 skóre modelu
    #            ppv:                Pozitivní prediktivní hodnota
    
    tn = confMatrix[0,0]
    tp = confMatrix[1,1]
    fp = confMatrix[1,0]
    fn = confMatrix[0,1]
    
    if (tp+fn)==0:
        se = np.nan()
    else:
        se = tp/(tp+fn)
    
    if (tn+fp) == 0:
        sp = np.nan()
    else:
        sp = tn/(tn+fp)
    
    if ( tp + fp ) == 0:
        ppv =  np.nan();       
    else:
        ppv = tp/( tp + fp )
   
        
    if ( tp + tn + fp + fn ) == 0:
        acc = np.nan()
    else:
        acc = ( tp + tn )/( tp + tn + fp + fn )
    
    
    if (tp + fn + fp) == 0:
        fScore =  np.nan()
    else:
        fScore = (2*tp) / (2*tp + fn + fp)
    
        
    return se,sp,acc,ppv,fScore
    