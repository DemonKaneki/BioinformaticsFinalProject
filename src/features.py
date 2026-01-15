import pandas as pd
import re

# Physical properties: [Hydropathy Score, Molecular Weight (Da), Chemical Charge]
aa_props = {
    'Ala': [1.8, 89.1, 0],   'Arg': [-4.5, 174.2, 1],  'Asn': [-3.5, 132.1, 0],
    'Asp': [-3.5, 133.1, -1], 'Cys': [2.5, 121.2, 0],   'Gln': [-3.5, 146.1, 0],
    'Glu': [-3.5, 147.1, -1], 'Gly': [-0.4, 75.1, 0],   'His': [-3.2, 155.2, 1],
    'Ile': [4.5, 131.2, 0],   'Leu': [3.8, 131.2, 0],   'Lys': [-3.9, 146.2, 1],
    'Met': [1.9, 149.2, 0],   'Phe': [2.8, 165.2, 0],   'Pro': [-1.6, 115.1, 0],
    'Ser': [-0.8, 105.1, 0],   'Thr': [-0.7, 119.1, 0],  'Trp': [-0.9, 204.2, 0],
    'Tyr': [-1.3, 181.2, 0],   'Val': [4.2, 117.1, 0]
}

def get_features(name_str):
    # Regex to extract p.Asn430Ser -> (Asn, 430, Ser)
    match = re.search(r'\(p\.([A-Z][a-z]{2})(\d+)([A-Z][a-z]{2})\)', str(name_str))
    if match:
        orig_aa, pos, new_aa = match.groups()
        if orig_aa in aa_props and new_aa in aa_props:
            # Calculate the Delta (The change the mutation causes)
            h_delta = aa_props[new_aa][0] - aa_props[orig_aa][0] # Hydropathy change
            w_delta = aa_props[new_aa][1] - aa_props[orig_aa][1] # Weight change
            c_delta = aa_props[new_aa][2] - aa_props[orig_aa][2] # Charge change
            return pd.Series([h_delta, w_delta, c_delta, int(pos)])
    return pd.Series([None, None, None, None])

print("Loading filtered data...")
df = pd.read_csv('filtered_clinvar.csv')

# 1. Map labels to binary: Pathogenic = 1, Benign = 0
df['Label'] = df['ClinicalSignificance'].apply(lambda x: 1 if 'pathogenic' in x.lower() else 0)

# 2. Extract the Bio-Features
print("Extracting physical delta features (this may take a minute)...")
df[['Hydro_Delta', 'Weight_Delta', 'Charge_Delta', 'Position']] = df['ProteinChange'].apply(get_features)

# 3. Drop rows that aren't protein-coding mutations (like row 3 in your head output)
df_final = df.dropna(subset=['Hydro_Delta'])

# 4. Save the final training set
df_final.to_csv('training_ready.csv', index=False)
print(f"Success! {len(df_final)} mutations ready for Deep Learning.")