import joblib

# Save the model and the scaler
joblib.dump(model, 'churn_predictor_model.pkl')
joblib.dump(scaler, 'feature_scaler.pkl')

print("Model and scaler saved successfully. Ready for deployment!")