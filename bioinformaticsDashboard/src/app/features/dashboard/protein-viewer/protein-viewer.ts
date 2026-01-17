import { Component, ElementRef, Input, OnChanges, OnInit, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import * as NGL from 'ngl';

@Component({
  selector: 'app-protein-viewer',
  templateUrl: './protein-viewer.html',
  styleUrls: ['./protein-viewer.css'],
  standalone: true,
  imports: [CommonModule]
})
export class ProteinViewerComponent implements OnInit, OnChanges {
  @ViewChild('viewport', { static: true }) viewport!: ElementRef;
  
  @Input() pdbId: string = '';
  @Input() mutationPosition: number | null = null;

  private stage: any;

  ngOnInit() {
    // Suppress THREE.js deprecation warning from NGL library
    const originalWarn = console.warn;
    console.warn = (...args) => {
      if (args[0]?.includes?.('useLegacyLights')) return;
      originalWarn.apply(console, args);
    };
    
    this.stage = new NGL.Stage(this.viewport.nativeElement, { backgroundColor: "#1a1a1a" });
    
    // Restore original console.warn after initialization
    setTimeout(() => console.warn = originalWarn, 2000);
    
    if (this.pdbId) {
      this.loadStructure();
    }
  }

  ngOnChanges() {
    if (this.stage && this.pdbId) {
      this.loadStructure();
    }
  }

  loadStructure() {
    this.stage.removeAllComponents();
    
    // Load from the public Protein Data Bank
    this.stage.loadFile(`rcsb://${this.pdbId}`).then((component: any) => {
      // Show the 'Cartoon' representation (the ribbon look)
      component.addRepresentation("cartoon", { color: "chainid" });
      
      // If we have a mutation position, highlight it!
      if (this.mutationPosition) {
        // Highlight the specific residue as a red ball-and-stick
        component.addRepresentation("ball+stick", {
          sele: `${this.mutationPosition}`, 
          color: "red",
          radius: 1.0
        });
        
        // Zoom the camera into that spot
        const duration = 1000;
        component.autoView(`${this.mutationPosition}`, duration);
      } else {
        component.autoView();
      }
    });
  }
}