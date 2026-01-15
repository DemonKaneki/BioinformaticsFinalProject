import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

# 1. Load the data
df = pd.read_csv('training_ready.csv')

# 2. Select our Features (X) and Target (y)
features = ['Hydro_Delta', 'Weight_Delta', 'Charge_Delta', 'Position']
X = df[features]
y = df['Label']

# 3. Split: 80% for training, 20% for testing the model's "intelligence"
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training on {len(X_train)} mutations...")

# 4. Initialize XGBoost Classifier
# We use scale_pos_weight if the data is imbalanced (more benign than pathogenic)
model = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    objective='binary:logistic',
    random_state=42
)

# 5. Train!
model.fit(X_train, y_train)

# 6. Evaluate
y_pred = model.predict(X_test)

print("\n--- Model Performance ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 7. Save the model for your Web App later
joblib.dump(model, 'snp_predictor_model.pkl')
print("\nModel saved as 'snp_predictor_model.pkl'")
