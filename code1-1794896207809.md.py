import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate a synthetic dataset of 1000 customers
data = {
    'CustomerID': range(1, 1001),
    'Age': np.random.randint(18, 70, 1000),
    'MonthlyCharge': np.random.uniform(20.0, 120.0, 1000),
    'TenureMonths': np.random.randint(1, 72, 1000),
    'ContractType': np.random.choice(['Month-to-month', 'One year', 'Two year'], 1000),
    'TechSupport': np.random.choice(['Yes', 'No'], 1000),
}

df = pd.DataFrame(data)

# Create a Churn target variable based on some logical rules (plus noise)
# Customers with short tenure, month-to-month contracts, and high charges are more likely to churn
churn_prob = np.where(df['ContractType'] == 'Month-to-month', 0.4, 0.1)
churn_prob += np.where(df['TenureMonths'] < 12, 0.2, 0.0)
churn_prob += np.where(df['TechSupport'] == 'No', 0.1, 0.0)
churn_prob = np.clip(churn_prob, 0, 1)

df['Churn'] = np.random.binomial(1, churn_prob)

print(df.head())