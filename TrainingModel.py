import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def train_model(preprocessedData,target_column ):

    selected_features = ['min', 'fgm'] # 'tov', 'stl', 'dreb']
    X = preprocessedData[selected_features]  # Признаки
    print("Shape of X after selecting features:", X.shape)

    y = target_column.apply(lambda x: 1 if x == 'yes' else 0)
    print("Shape of y after selecting features:", y.shape)

    # Логистическая регрессия
    #model = LogisticRegression(max_iter=20)
    #model.fit(X, y)                                     #Я В ДУШЕ НЕ ЗНАЮ, ПОЧЕМУ ОНО ЗАСЕКАЕТСЯ НА ЭТОЙ СТРОКЕ ИЗ-ЗА ПУСТЫХ ПЕРЕМЕННЫХ
                                    #ПОТОМУ ЧТО Я СПЕЦИАЛЬНО ВЫПРИНТЛА Х И У ПЕРЕД ТЕМ, КАК ЗАСУНУ ИХ В МОДЕЛЬ И ТАМ РАЗМЕРЫ   Shape of X after selecting features: (599, 2)
                                    #   интернет говорит, что 1размерность у это вроде норм я хз                               Shape of y after selecting features: (599,)

    #return model

