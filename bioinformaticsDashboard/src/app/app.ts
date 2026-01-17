import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProteinDataService } from './core/services/protein-data';
import { Header } from './shared/components/header/header';
import { VcfUpload } from './features/dashboard/vcf-upload/vcf-upload';
import { MutationList } from './features/dashboard/mutation-list/mutation-list';
import { ProteinViewerComponent } from './features/dashboard/protein-viewer/protein-viewer';
import { NeuralAnimation } from './features/dashboard/neural-animation/neural-animation';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    Header,
    VcfUpload,
    MutationList,
    ProteinViewerComponent,
    NeuralAnimation
  ],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class AppComponent {
  scanResults: any[] = [];
  selectedMutation: any = null;
  selectedPdbId: string = '';
  selectedPosition: number | null = null;

  constructor(private proteinService: ProteinDataService) {}

  // 1. Triggered when Python API returns JSON
  onResults(data: any) {
    this.scanResults = data.results;
  }

  // 2. Triggered when you click a mutation in the list
  onMutationSelect(mutation: any) {
    this.selectedMutation = mutation;
    this.selectedPosition = mutation.position;
    this.selectedPdbId = this.proteinService.getPdbId(mutation.gene);
  }
}