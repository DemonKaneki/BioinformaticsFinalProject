from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
import io
import re

app = FastAPI()

# Allow Angular to talk to this Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the artifacts we built
model = joblib.load('model/snp_predictor_model.pkl')

# Amino Acid Reference (The "Bio-Dictionary")
aa_props = {
    'Ala': [1.8, 89.1, 0],   'Arg': [-4.5, 174.2, 1],  'Asn': [-3.5, 132.1, 0],
    'Asp': [-3.5, 133.1, -1], 'Cys': [2.5, 121.2, 0],   'Gln': [-3.5, 146.1, 0],
    'Glu': [-3.5, 147.1, -1], 'Gly': [-0.4, 75.1, 0],   'His': [-3.2, 155.2, 1],
    'Ile': [4.5, 131.2, 0],   'Leu': [3.8, 131.2, 0],   'Lys': [-3.9, 146.2, 1],
    'Met': [1.9, 149.2, 0],   'Phe': [2.8, 165.2, 0],   'Pro': [-1.6, 115.1, 0],
    'Ser': [-0.8, 105.1, 0],   'Thr': [-0.7, 119.1, 0],  'Trp': [-0.9, 204.2, 0],
    'Tyr': [-1.3, 181.2, 0],   'Val': [4.2, 117.1, 0]
}

def extract_features_from_str(mutation_str):
    # Regex to handle VCF style strings: p.Arg175His or (p.Arg175His)
    match = re.search(r'p\.([A-Z][a-z]{2})(\d+)([A-Z][a-z]{2})', mutation_str)
    if match:
        orig_aa, pos, new_aa = match.groups()
        if orig_aa in aa_props and new_aa in aa_props:
            h_delta = aa_props[new_aa][0] - aa_props[orig_aa][0]
            w_delta = aa_props[new_aa][1] - aa_props[orig_aa][1]
            c_delta = aa_props[new_aa][2] - aa_props[orig_aa][2]
            return [h_delta, w_delta, c_delta, int(pos)], (orig_aa, new_aa)
    return None, None

@app.post("/scan-vcf")
async def scan_vcf(file: UploadFile = File(...)):
    content = await file.read()
    decoded = content.decode("utf-8")
    
    # Simple VCF Parser (Skipping headers)
    lines = [l for l in decoded.split('\n') if l and not l.startswith('##')]
    df = pd.read_csv(io.StringIO('\n'.join(lines)), sep='\t')
    
    # We look for a column typically named 'INFO' or 'ID' that contains the p. mutation
    # In a real VCF, this requires "Variant Effect Predictor" (VEP) output
    pathogenic_variants = []
    
    for _, row in df.iterrows():
        # Searching the 'INFO' column for the protein change
        info_str = str(row.get('INFO', ''))
        features, aa_pair = extract_features_from_str(info_str)
        
        if features:
            # Predict
            prob = model.predict_proba([features])[0][1] # Probability of being Pathogenic
            if prob > 0.5:
                pathogenic_variants.append({
                    "mutation": f"p.{aa_pair[0]}{features[3]}{aa_pair[1]}",
                    "probability": float(prob),
                    "deltas": {
                        "hydro": features[0],
                        "weight": features[1],
                        "charge": features[2]
                    },
                    "position": features[3],
                    "gene": row.get('ID', 'Unknown')
                })
                
    return {"status": "success", "count": len(pathogenic_variants), "results": pathogenic_variants}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
