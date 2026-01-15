import pandas as pd
import xgboost as xgb
import joblib
import shap
import matplotlib.pyplot as plt

# 1. Load data and model
df = pd.read_csv('training_ready.csv')
model = joblib.load('snp_predictor_model.pkl')

features = ['Hydro_Delta', 'Weight_Delta', 'Charge_Delta', 'Position']
X = df[features]

# 2. Initialize SHAP explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# 3. Create the Summary Plot
plt.figure(figsize=(10, 6))
shap.summary_plot(shap_values, X, show=False)
plt.title("Biological Feature Impact on Pathogenicity")
plt.savefig('model_explanation.png')
print("Explanation plot saved as 'model_explanation.png'")
plt.show()
