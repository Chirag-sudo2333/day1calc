import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline

df = pd.read_csv('/Users/macair45/Downloads/Titanic-Dataset.csv')
df = df.drop(columns=['Cabin'])


df['Age'] = df['Age'].fillna(np.mean(df['Age']))
df['Fare'] = df['Fare'].fillna(np.mean(df['Fare']))


df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)


df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)


df = df.drop(columns=['Name', 'Ticket', 'PassengerId'])


X = df.drop(columns=['Survived'])
y = df['Survived']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression())
])


pipeline.fit(X_train, y_train)


y_pred = pipeline.predict(X_test)
from sklearn.metrics import accuracy_score
print("Test accuracy:", accuracy_score(y_test, y_pred))


cv_scores = cross_val_score(pipeline, X, y, cv=5)
print("All CV scores:", cv_scores)
print("Mean CV accuracy:", cv_scores.mean())
