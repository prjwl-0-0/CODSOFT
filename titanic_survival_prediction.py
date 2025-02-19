# -*- coding: utf-8 -*-
"""TITANIC SURVIVAL PREDICTION.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xJ7d0dCLU7CvqDDu0hBhXsKxxOLwRw2W
"""

from google.colab import files

uploaded = files.upload()

import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
df.head()

df['Age'].fillna(df['Age'].median(), inplace=True)


df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})


df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)


df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

import pandas as pd

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Fill missing Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Convert 'Sex' to numeric (0 = female, 1 = male)
df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})

# Fill missing Embarked with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Convert 'Embarked' to numerical values using one-hot encoding
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Drop unnecessary columns
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

df.head()  # Verify changes

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Define features and target
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

df['Predicted_Survival'] = model.predict(X)
df[['Predicted_Survival']].to_csv("Titanic_Predictions.csv", index=False)

# Download file
from google.colab import files
files.download("Titanic_Predictions.csv")

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Train Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predict
rf_pred = rf_model.predict(X_test)

# Evaluate
rf_accuracy = accuracy_score(y_test, rf_pred)
print(f"Random Forest Accuracy: {rf_accuracy:.2f}")

!pip install xgboost  # Install XGBoost if not installed

import xgboost as xgb

# Train XGBoost model
xgb_model = xgb.XGBClassifier(n_estimators=100, use_label_encoder=False, eval_metric='logloss')
xgb_model.fit(X_train, y_train)

# Predict
xgb_pred = xgb_model.predict(X_test)

# Evaluate
xgb_accuracy = accuracy_score(y_test, xgb_pred)
print(f"XGBoost Accuracy: {xgb_accuracy:.2f}")

print(f"Logistic Regression Accuracy: {accuracy:.2f}")
print(f"Random Forest Accuracy: {rf_accuracy:.2f}")
print(f"XGBoost Accuracy: {xgb_accuracy:.2f}")

# Predict survival using the trained XGBoost model
df['Predicted_Survival'] = xgb_model.predict(X)
df[['Predicted_Survival']].head()  # Preview predictions

# Save predictions to a CSV file
df[['Predicted_Survival']].to_csv("Titanic_Predictions_XGBoost.csv", index=False)

# Download the file in Colab
from google.colab import files
files.download("Titanic_Predictions_XGBoost.csv")

from google.colab import files
uploaded = files.upload()  # Manually upload Titanic_Predictions_XGBoost.csv

import pandas as pd

# Read the CSV file
df_predictions = pd.read_csv("Titanic_Predictions_XGBoost.csv")

# Show first few rows
df_predictions.head()