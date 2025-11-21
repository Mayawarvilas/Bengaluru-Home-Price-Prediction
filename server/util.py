import numpy as np
import json
import pickle

__locations=None
__data_columns=None
__model=None

def get_estimted_price(location,sqft,bath,bhk):
   
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1

    X=np.zeros(len(__data_columns))
    X[0]=sqft
    X[1]=bath
    X[2]=bhk

    if loc_index >=0:
        X[loc_index]=1
    
    return round(__model.predict([X])[0],2)

def get_location_names():
    return __locations

def load_save_artifactes():
    print('loading artifacts are runing')
    global __locations
    global __data_columns
    global __model

    with open("./artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]
    
    with open("./artifacts/bengaluru_house_price_model.pickle",'rb') as f:
        __model=pickle.load(f)

    print('artifactes are loaded')


if __name__=='__main__':
    load_save_artifactes()
    print(get_location_names())
    print(get_estimted_price('1st phase jp nagar',1000,2,2))
    print(get_estimted_price('1st phase jp nagar',1000,2,3))
    print(get_estimted_price('akshaya nagar',1000,2,2))
    print(get_estimted_price('anjanapura',1000,2,2))