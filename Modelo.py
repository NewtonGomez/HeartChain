import pandas as pd #Analizar datos
import numpy as np # Algebra linear
import seaborn as sns #Graficas
import matplotlib.pyplot as plt #Graficas
sns.set(style = 'whitegrid') #Establecer fondo a las graficas
from scipy.stats import skew, kurtosis #Analisis estadistico
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression