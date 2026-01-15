from fastapi import FastAPI, UploadFile
import joblib
import pandas as pd
from feature_engineering import extract_features # The script we wrote earlier

app = FastAPI()
model = joblib.load('snp_predictor_model.pkl')

@app.post("/analyze-vcf")
async def analyze_vcf(file: UploadFile):
    # 1. Parse VCF
    # 2. Run through model
    # 3. Return JSON with 'Pathogenic' variants
    return {"results": [...]}

@app.get("/prediction-logic/{mutation}")
async def get_logic(mutation: str):
    # This returns the specific Hydro/Weight/Charge deltas 
    # so your Angular app can show them in the UI
    features = extract_features(mutation) 
    prob = model.predict_proba(features)
    return {"deltas": features, "probability": prob}
