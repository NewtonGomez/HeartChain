import pandas as pd
import numpy as np
from statistics import mode
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from scipy.sparse import data
import seaborn as sns
import matplotlib.pyplot as plt

class model():
    def __init__(self) -> None: 
        self.data_df = pd.read_csv('C:/Users/Juanp/OneDrive/Documentos/ECG_AHORA_SI/MIT-BIH Arrhythmia Database.csv/MIT-BIH Arrhythmia Database.csv')
        self.x_data = self.data_df.drop(columns = ['record', 'type'])
        self.y_label = self.data_df[['type']]
        self.y_label.replace(1, 'Arritmia', inplace=True)
        self.y_label.replace(0, 'Sano', inplace=True)
        self.X_train, X_test, y_train, y_test = train_test_split(self.x_data, self.y_label, random_state=101)
        self.min_max_scaler = preprocessing.MinMaxScaler()
        self.X_train_scaled = self.min_max_scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.min_max_scaler.transform(X_test)
        self.model = RandomForestClassifier(random_state=101, n_estimators=150)
        self.model.fit(self.X_train_scaled, y_train)

    def predecir(self, ecg):
        return model.predict(ecg)


