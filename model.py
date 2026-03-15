import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Dataset with Skin, Mental & Respiratory
raw_data = {
    'diseases': ['Fungal infection', 'Acne', 'Psoriasis', 'Eczema', 'Asthma', 'Bronchitis', 'Anxiety', 'Depression', 'Common Cold', 'Insomnia'],
    'itching': [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    'skin rash': [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    'cough': [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    'shortness of breath': [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    'anxiety and nervousness': [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    'insomnia': [0, 0, 0, 0, 0, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(raw_data)
X = df.drop("diseases", axis=1)
y = df["diseases"]

model = DecisionTreeClassifier()
model.fit(X, y)

# Save Files
with open("disease_model.pkl", "wb") as f:
    pickle.dump(model, f)
df.to_csv("Disease and symptoms dataset.xls", index=False)
print("✅ Step 1: Model trained without errors!")