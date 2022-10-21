import pandas as pd
import numpy as np
import json
from sklearn.linear_model import LinearRegression
import preprocessing.cleaning_data
from preprocessing.cleaning_data import Cleaning
import pickle


class Prediction:

    def __init__(self) -> None:
        pass
    
    def predict(self, json_file):
        self = Cleaning()
        self = self.preprocess(json_file)
        df = self.df
        status_code = self.status_code

        with open('model/regressor_param.json', 'r') as file:
                dict_ = json.load(file)

        model = LinearRegression()
        model.coef_ = np.array(dict_.get('coef'))
        model.intercept_ = dict_.get('intercept')
        
        # pkl_immo_model = "model/pkl_immo_model.pkl"
        # with open(pkl_immo_model, 'rb') as file:
        #     pickle_model = pickle.load(file)



        output = {}
        output['prediction']= model.predict(df)[0]
        output['status_code']= status_code
        return output