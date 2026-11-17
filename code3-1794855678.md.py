from sklearn.preprocessing import LabelEncoder, StandardScaler

# Drop unnecessary columns
df = df.drop('CustomerID', axis=1)

# Encode categorical variables
categorical_cols = ['ContractType', 'TechSupport']
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Separate features (X) and target label (y)
X = df_encoded.drop('Churn', axis=1)
y = df_encoded['Churn']

# Scale numerical features (Age, MonthlyCharge, TenureMonths)
scaler = StandardScaler()
X[['Age', 'MonthlyCharge', 'TenureMonths']] = scaler.fit_transform(X[['Age', 'MonthlyCharge', 'TenureMonths']])

print(X.head())