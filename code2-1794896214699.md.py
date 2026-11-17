import seaborn as sns
import matplotlib.pyplot as plt

# 1. Check for missing values (Our synthetic data has none, but this is a standard step)
print(df.isnull().sum())

# 2. Visualize the target variable balance
sns.countplot(x='Churn', data=df)
plt.title('Customer Churn Distribution')
plt.show()

# 3. Analyze Churn rate by Contract Type
sns.barplot(x='ContractType', y='Churn', data=df)
plt.title('Churn Rate by Contract Type')
plt.show()