import { Component, Input, OnChanges, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-neural-animation',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './neural-animation.html',
  styleUrl: './neural-animation.css',
})
export class NeuralAnimation implements OnChanges, OnDestroy {
  @Input() active: boolean = false;
  
  inputNodes = Array(4).fill(null);   // 4 input features
  hiddenNodes = Array(6).fill(null);  // 6 hidden neurons
  
  isProcessing: boolean = false;
  isComplete: boolean = false;
  
  private processingTimeout: any;

  ngOnChanges() {
    if (this.active && !this.isProcessing && !this.isComplete) {
      this.startProcessing();
    } else if (!this.active) {
      this.reset();
    }
  }

  ngOnDestroy() {
    if (this.processingTimeout) {
      clearTimeout(this.processingTimeout);
    }
  }

  private startProcessing() {
    this.isProcessing = true;
    this.isComplete = false;
    
    // Simulate neural network processing time
    this.processingTimeout = setTimeout(() => {
      this.isProcessing = false;
      this.isComplete = true;
    }, 3000); // 3 second processing simulation
  }

  private reset() {
    this.isProcessing = false;
    this.isComplete = false;
    if (this.processingTimeout) {
      clearTimeout(this.processingTimeout);
      this.processingTimeout = null;
    }
  }

  get statusText(): string {
    if (this.isProcessing) return 'Processing...';
    if (this.isComplete) return 'Complete';
    return 'Idle';
  }
}
