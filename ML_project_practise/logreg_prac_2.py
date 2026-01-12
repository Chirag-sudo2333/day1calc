import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
scale = StandardScaler()
def dataset():
    data = {
        "Age": [
            22, 25, 28, 30, 35, 40, 45, 50, 23, 27,
            32, 38, 42, 48, 29, 34, 37, 41, 46, 52,
            24, 26, 31, 36, 39, 44, 49, 54, 21, 33,
            35, 28, 47, 51, 43, 38, 26, 29, 45, 50
        ],

        "Education": [
            "High School", "Bachelor", "Bachelor", "Master", "Master",
            "PhD", "PhD", "PhD", "High School", "Bachelor",
            "Master", "Master", "PhD", "PhD", "Bachelor",
            "Master", "Master", "PhD", "PhD", "PhD",
            "High School", "Bachelor", "Bachelor", "Master", "Master",
            "PhD", "PhD", "PhD", "High School", "Master",
            "Master", "Bachelor", "PhD", "PhD", "PhD",
            "Master", "Bachelor", "Bachelor", "PhD", "PhD"
        ],

        "Skill_Score": [
            70, 82, 65, 90, 55, 80, None, 88, 60, 72,
            85, None, 77, 93, 68, 81, 76, 79, 84, 91,
            63, 71, 69, 87, 74, None, 90, 95, 58, 66,
            72, 75, 89, 92, 83, 78, 69, 71, None, 88
        ],

        "Salary": [
            25000, 30000, 35000, 48000, 52000, 75000, 80000, 90000,
            22000, 34000, 50000, 60000, None, 95000, 37000, 52000,
            58000, 78000, 88000, 110000, 21000, 31000, None, 50000,
            58000, 82000, 97000, 115000, 19000, 54000, 60000, 36000,
            92000, 108000, 86000, 57000, 34000, 38000, None, 102000
        ],

        "Hired": [
            0, 1, 1, 1, 0, 1, 1, 1, 0, 1,
            1, 1, 0, 1, 0, 1, 1, 1, 1, 1,
            0, 1, 0, 1, 1, 1, 1, 1, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 0, 1, 1
        ]
    }
    edu_key = {
        'High School' : 0,
        'Bachelor' : 1,
        'Master' : 2,
        'PhD' : 3
    }
    return data, edu_key
data_dict, edu_key_dict = dataset()
df = pd.DataFrame(data_dict)
df['Education'] = df['Education'].map(edu_key_dict)
df['Skill_Score'] = df['Skill_Score'].fillna(np.mean(df['Skill_Score']))
df['Salary'] = df['Salary'].fillna(np.mean(df['Salary']))
print(np.sum(df.isnull()))
model = LogisticRegression()
X, y = (df.drop(columns=['Hired'])).to_numpy(), (df['Hired']).to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3, stratify=y)
X_train_scaled = scale.fit_transform(X_train)
X_test_scaled = scale.transform(X_test)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
print(model.predict_proba(X_test_scaled))
print(y_pred, y_test)
print('Accuracy is ', 100*accuracy_score(y_pred, y_test), '%.')

