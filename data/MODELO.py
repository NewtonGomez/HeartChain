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

data_df = pd.read_csv('C:/Users/Juanp/OneDrive/Documentos/ECG_AHORA_SI/MIT-BIH Arrhythmia Database.csv/MIT-BIH Arrhythmia Database.csv')

x_data = data_df.drop(columns = ['record', 'type'])
y_label = data_df[['type']]

y_label.replace(1, 'Arritmia', inplace=True)
y_label.replace(0, 'Sano', inplace=True)

X_train, X_test, y_train, y_test = train_test_split(x_data, y_label, random_state=101)

min_max_scaler = preprocessing.MinMaxScaler()
X_train_scaled = min_max_scaler.fit_transform(X_train)
X_test_scaled = min_max_scaler.transform(X_test)

model = RandomForestClassifier(random_state=101, n_estimators=150)
model.fit(X_train_scaled, y_train)

carac = x_data[x_data.index == 55]

y_predict_test=model.predict(carac)
print(f'El paciente esta clasificado como: {y_predict_test}')


