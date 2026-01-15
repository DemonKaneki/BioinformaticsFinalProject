import pandas as pd

def process_clinvar_large(file_path, output_csv):
    chunk_size = 100000
    first_chunk = True

    useful_cols = [
        '#AlleleID', 
        'Type', 
        'Name', 
        'GeneSymbol', 
        'ClinicalSignificance', 
        'RS# (dbSNP)', 
        'Assembly'
    ]

    print("Starting data extraction...")

    for chunk in pd.read_csv(file_path, sep='\t', compression='gzip',
                             usecols=useful_cols, chunksize=chunk_size, low_memory=False):

        # 1. Filter for Human Genome Build 38
        chunk = chunk[chunk['Assembly'] == 'GRCh38']

        # 2. Filter for single-letter changes
        chunk = chunk[chunk['Type'] == 'single nucleotide variant']

        # 3. Filter for clear labels
        valid_labels = ['Pathogenic', 'Benign', 'Likely pathogenic', 'Likely benign']
        chunk = chunk[chunk['ClinicalSignificance'].isin(valid_labels)]

        # Rename 'Name' to 'ProteinChange' so the next scripts work
        chunk = chunk.rename(columns={'Name': 'ProteinChange'})

        # Write to CSV
        chunk.to_csv(output_csv, mode='a', index=False, header=first_chunk)
        first_chunk = False
        print(f"Processed a chunk... rows saved so far: {len(chunk)}")

    print(f"Done! Cleaned data saved to {output_csv}")

if __name__ == "__main__":
    process_clinvar_large('variant_summary.txt.gz', 'filtered_clinvar.csv')