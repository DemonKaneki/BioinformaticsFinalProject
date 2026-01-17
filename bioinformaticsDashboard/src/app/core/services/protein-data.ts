import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class ProteinDataService {
  // Mapping Gene Symbols to PDB IDs
  private geneToPdbMap: { [key: string]: string } = {
    'TP53': '1TUP',   // Tumor protein p53
    'BRCA2': '1MIU',  // Breast cancer type 2
    'BRCA1': '1JNX',  // Breast cancer type 1
    'HFE': '1A6Z',    // Hemochromatosis protein
    'LDLR': '1N7D'    // LDL Receptor
  };

  getPdbId(geneSymbol: string): string {
    return this.geneToPdbMap[geneSymbol.toUpperCase()] || '1TUP';
  }
}