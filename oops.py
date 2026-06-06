import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score , root_mean_squared_error , mean_squared_error
import sys
import os
import pickle
import warnings
warnings.filterwarnings("ignore")

class MLR:
    def __init__(self , path):
        try:
            self.path = path
            self.df = pd.read_csv(self.path)
            self.df = pd.get_dummies(self.df , columns = ['Extracurricular Activities'], drop_first = True)
            self.df.head()
            self.df.isnull()
            self.df.info()
            self.X = self.df.iloc[:,:-1]
            self.y = self.df.iloc[:,-1]
            self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X , self.y ,test_size=0.2 , random_state=42)
        except Exception as e:
            er_type,er_lineno,er_message = sys.exc_info()
            print(f"Error type : {er_type} line : {er_lineno} occur : {er_message}")

    def training(self):
        try:
            self.reg = LinearRegression()
            self.reg.fit(self.X_train , self.y_train)
            print(f"Training Accuracy : {r2_score(self.y_train , self.reg.predict(self.X_train))}")
            print(f"Training loss :{mean_squared_error(self.y_train , self.reg.predict(self.X_train))}")
            print(f"Training loss :{root_mean_squared_error(self.y_train, self.reg.predict(self.X_train))}")
        except Exception as e:
            er_type,er_lineno,er_message = sys.exc_info()
            print(f"Error type : {er_type} line : {er_lineno} occur : {er_message}")

    def testing(self):
        try :
            print(f"Test Accuracy : {r2_score(self.y_test, self.reg.predict(self.X_test))}")
            print(f"Test loss :{mean_squared_error(self.y_test, self.reg.predict(self.X_test))}")
            print(f"Test loss :{root_mean_squared_error(self.y_test, self.reg.predict(self.X_test))}")
        except Exception as e:
            er_type,er_lineno,er_message = sys.exc_info()
            print(f"Error type : {er_type} line : {er_lineno} occur : {er_message}")

    def Sample_prediction_testing(self , Hours_studied, Previous_score, Extracurricular_Activities, sleep_hours, practised_questions):
        try :
            result = self.reg.predict([[Hours_studied , Previous_score ,Extracurricular_Activities , sleep_hours, practised_questions]])[0]
            print(f"Sample Prediction Testing : {result}")
        except Exception as e:
            er_type,er_lineno,er_message = sys.exc_info()
            print(f"Error type : {er_type} line : {er_lineno} occur : {er_message}")

    def save_model(self):
        try :
            with open("Model_pkl.pkl" , 'wb') as f:
                pickle.dump(self.reg , f)
            print("file saved successfully")
        except Exception as e:
            er_type,er_lineno,er_message = sys.exc_info()
            print(f"Error type : {er_type} line : {er_lineno} occur : {er_message}")


if __name__ == '__main__':
    obj = MLR("D:\Regression\Student_Performance_Regression\Student_Performance.csv")
    obj.training()
    obj.testing()
    obj.Sample_prediction_testing(5,70,1,7,5)
    obj.save_model()



