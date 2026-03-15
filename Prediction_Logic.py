import pickle
import pandas as pd
import numpy as np

def predict_disease(user_input_list):
    try:
        with open("disease_model.pkl", "rb") as f:
            model = pickle.load(f)
        data = pd.read_csv("Disease and symptoms dataset.xls")
        cols = list(data.columns.drop("diseases"))

        vector = np.zeros(len(cols))
        # Combine all inputs into one string for better matching
        input_string = " ".join(user_input_list).lower()

        match = False
        for i, symptom in enumerate(cols):
            if symptom.lower() in input_string:
                vector[i] = 1
                match = True

        if not match: return "Unknown", 0.0

        res = model.predict([vector])[0]
        conf = np.max(model.predict_proba([vector])) * 100
        return res, conf
    except:
        return "Unknown", 0.0