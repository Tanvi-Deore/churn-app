import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

def predict(input_data_dict):
    df = pd.DataFrame([input_data_dict])
    
    # Convert to dummy
    df = pd.get_dummies(df)
    
    # Match columns
    df = df.reindex(columns=columns, fill_value=0)
    
    result = model.predict(df)
    return int(result[0])