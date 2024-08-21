# ============================= IMPORT LIBRARIES =============================

import pandas as pd
from sklearn import preprocessing
import warnings

warnings.filterwarnings("ignore")

# ============================= DATA SELECTION ==============================

dataframe = pd.read_csv("complete_dataset.csv")

print("----------------------------------------------------")
print("Input Data          ")
print("----------------------------------------------------")
print()
print(dataframe.head(20))
print()

# ============================= PREPROCESSING ==============================

# ==== CHECKING MISSING VALUES ====

print("----------------------------------------------------")
print("Before checking Missing Values          ")
print("----------------------------------------------------")
print()
print(dataframe.isnull().sum())
print()

print("----------------------------------------------------")
print("After checking Missing Values          ")
print("----------------------------------------------------")
print()
dataframe = dataframe.fillna(dataframe.mean())
print(dataframe.isnull().sum())
print()

# === DROP UNWANTED COLUMNS ====

dataframe = dataframe.drop('date', axis=1)
print()

# === LABEL ENCODING ===

print("----------------------------------------------------")
print("Before Label Encoding          ")
print("----------------------------------------------------")
print()
print(dataframe['school_day'].head(15))
print()
label_encoder = preprocessing.LabelEncoder()

print("----------------------------------------------------")
print("After Label Encoding          ")
print("----------------------------------------------------")
print()
dataframe['school_day'] = label_encoder.fit_transform(dataframe['school_day'])
dataframe['holiday'] = label_encoder.fit_transform(dataframe['holiday'])

print(dataframe['school_day'].head(15))

# ============================= DATA SPLITTING ==============================

print("----------------------------------------------------")
print("Data Splitting          ")
print("----------------------------------------------------")
print()

from sklearn.model_selection import train_test_split

X = dataframe.drop('RRP', axis=1)
y = dataframe['RRP']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

print("Total no of data's       :", dataframe.shape[0])
print()
print("Total no of Train data's :", X_train.shape[0])
print()
print("Total no of Test data's  :", X_test.shape[0])
print()
print()

# ============================= CLASSIFICATION ==============================

# ==== LASSO REGRESSION ====

from sklearn import linear_model

lasso_r = linear_model.Lasso()

lasso_r.fit(X_train, y_train)

pred_lasso = lasso_r.predict(X_test)

from sklearn import metrics

mae_lr = metrics.mean_absolute_error(pred_lasso, y_test)

mse_lr = metrics.mean_squared_error(pred_lasso, y_test)

import math

rsme_lr = math.sqrt(mse_lr)

print("---------------------------------------")
print("Machine Learning ----> Lasso Regression")
print("---------------------------------------")
print()
print("==================================================")
print("1. Mean Absolute Error     :", mae_lr)
print()
print("2. Mean Squared Error      :", mse_lr)
print()
print("3. Root Mean Squared Error :", rsme_lr)
print("==================================================")
print()

# ==== RIDGE REGRESSION ====

ridge_r = linear_model.Ridge()

ridge_r.fit(X_train, y_train)

pred_ridge = ridge_r.predict(X_test)

mae_rr = metrics.mean_absolute_error(pred_ridge, y_test)

mse_rr = metrics.mean_squared_error(pred_ridge, y_test)

import math

rsme_rr = math.sqrt(mse_rr)

print("---------------------------------------")
print("Machine Learning ----> Ridge Regression")
print("---------------------------------------")
print()
print("==================================================")
print("1. Mean Absolute Error     :", mae_rr)
print()
print("2. Mean Squared Error      :", mse_rr)
print()
print("3. Root Mean Squared Error :", rsme_rr)
print("==================================================")
print()

# ============================= PREDICTION ==============================

# === ELECTRICITY PRICE ===

print("---------------------------------------")
print("Prediction ---> Electricity Price")
print("---------------------------------------")
print()

for i in range(0, 10):
    print("-------------------------------")
    print()
    print([i], "The Electricity price =", pred_lasso[i])

print()
print("---------------------------------------------------------------")
print()

import matplotlib.pyplot as plt

plt.title("Predicting Electricity Price")
plt.plot(pred_lasso)
plt.show()

print()
print("------------------------------------------------------------")
print()

# === COMPARISON ===

import matplotlib.pyplot as plt
import numpy as np

objects = ('Lasso Regression', 'Ridge Regression')
y_pos = np.arange(len(objects))
performance = [mae_lr, mae_rr]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Performance ')
plt.title('Comparison Graph -- Error Values')
plt.show()
