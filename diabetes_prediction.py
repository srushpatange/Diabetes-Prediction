# -*- coding: utf-8 -*-
"""Diabetes_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z_zMwM1U1hBLt_Mz9ypWQR2OUwtmnQpD
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler #(standardize data to common range)
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Loading the diabetes dataset to pandas dataframe
df=pd.read_csv("/content/diabetes.csv")

df.head()

# statistical measure of data
df.describe()

df["Outcome"].value_counts()

df.shape

df.groupby("Outcome").mean()

# all data except labels
X= df.drop(columns="Outcome",axis=1)
y=df["Outcome"]

print(X)

print(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,stratify=y, random_state=2)

print(X.shape,X_train.shape,X_test.shape)

classifier=svm.SVC(kernel='linear')

classifier.fit(X_train,y_train)

# accuracy_score of training data

X_train_prediction=classifier.predict(X_train)
training_data_accuracy_score=accuracy_score(y_train,X_train_prediction)
print(f"Accuracy Score of training data : {training_data_accuracy_score * 100} %")

# accuracy_score of testing data

X_test_prediction=classifier.predict(X_test)
testing_data_accuracy_score=accuracy_score(y_test,X_test_prediction)
print(f"Accuracy Score of testing data : {testing_data_accuracy_score * 100} %")

import pickle

filename="diabetesmodel.sav"
pickle.dump(classifier,open(filename,'wb'))

# loading the saved model
loaded_model=pickle.load(open("diabetesmodel.sav",'rb'))

# 1,85,66,29,0,26.6,0.351,31,0
# 8,183,64,0,0,23.3,0.672,32,1
input_data=(1,85,66,29,0,26.6,0.351,31)

# change input_data to numpy array
inp_data_as_numpy_arr=np.asarray(input_data)
print(f"1D Data : {inp_data_as_numpy_arr}\n")

# input data reshape because model is expecting 2D array or all data , we'll reshape our 1d data to 2d and feed our model an instance
inp_data_reshape=inp_data_as_numpy_arr.reshape(1,-1)
print(f"2D Data : {inp_data_reshape}\n")

# standardize the input data
# std_data=scaler.transform(inp_data_reshape)
# print(f"Standardized Data : {std_data}\n")
# prediction
prediction = loaded_model.predict(inp_data_reshape)
print(f"Predicted Value: {prediction}")
if(prediction[0]==0):
    print("This person is Non-Diabetic")
else:
    print("This person is Diabetic")

