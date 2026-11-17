from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Make predictions on the unseen test set
y_pred = model.predict(X_test)

# 1. Accuracy
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}\n")

# 2. Classification Report (Precision, Recall, F1-Score)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 3. Confusion Matrix Visualization
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

# 4. Feature Importance (What drives churn?)
importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nFeature Importances:")
print(importances)