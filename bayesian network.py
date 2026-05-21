import pandas as pd
import numpy as np
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

# 1. Load dataset
data = pd.read_csv("heart.csv")

# Remove missing values
data = data.replace('?', np.nan).dropna()

# Convert continuous data into categories
data['age'] = pd.cut(
    data['age'],
    bins=[0, 45, 60, 100],
    labels=[0, 1, 2]
).astype(int)

data['trestbps'] = pd.cut(
    data['trestbps'],
    bins=[0, 130, 200],
    labels=[0, 1]
).astype(int)

data['chol'] = pd.cut(
    data['chol'],
    bins=[0, 200, 240, 600],
    labels=[0, 1, 2]
).astype(int)

# Convert target into binary
data['Heartdisease'] = data['Heartdisease'].apply(
    lambda x: 1 if x > 0 else 0
)

# 2. Create Bayesian Network
model = BayesianNetwork([
    ('age', 'trestbps'),
    ('trestbps', 'Heartdisease'),
    ('chol', 'Heartdisease')
])

# 3. Train model
model.fit(data, estimator=MaximumLikelihoodEstimator)

# 4. Inference
infer = VariableElimination(model)

# Prediction
q = infer.query(
    variables=['Heartdisease'],
    evidence={'age': 0}
)

print(q)
