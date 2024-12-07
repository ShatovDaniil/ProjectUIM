import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, KFold
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler
from DataPreprocessing import DataPreprocessing
from joblib import dump
import os
from DataPreprocessing import DataPreprocessing

def train_model(preprocessedData):
    X = preprocessedData.drop(columns=['target_5yrs', 'Var1', 'name'])

    y = preprocessedData['target_5yrs']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = LogisticRegression(max_iter=1000)

    #kf = KFold(n_splits=5, shuffle=True, random_state=0)
    #cv_results = cross_val_score(model, X_train, y_train, cv=kf, scoring='accuracy')

    #y = cross_val_predict(model, X_train, y_train, cv=kf)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)



    output_dir = r"C:\Users\MagicBook\PycharmProjects\pythonProject\ProjectUIM"  # Путь к вашей папке ProjectUIM
    os.makedirs(output_dir, exist_ok=True)  # Создаем директорию, если она не существует
    model_filename = os.path.join(output_dir, 'trained_model.joblib')  # Указываем путь для сохранения модели
    dump(model, model_filename)  # Сохраняем модель в файл

    print(f"Модель сохранена по пути: {model_filename}")
    return model

filePath = "C:\\Users\\MagicBook\\PycharmProjects\\pythonProject\\ProjectUIM"
inputData = pd.read_csv(f"{filePath}\\TrainNBAData.csv")
df = DataPreprocessing(inputData)
train_model(df)