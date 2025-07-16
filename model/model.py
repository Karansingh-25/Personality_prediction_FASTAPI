import pickle 
import pandas as pd


with open("model/model.pkl",'rb') as f:
    model=pickle.load(f)

MODEL_VERSION='1.0.0'

def predict(userInput:dict):
    input_df=pd.DataFrame([userInput])

    output=model.predict(input_df)[0]

    return output