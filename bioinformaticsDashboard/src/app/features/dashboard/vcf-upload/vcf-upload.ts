import { Component, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-vcf-upload',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './vcf-upload.html',
  styleUrl: './vcf-upload.css',
})
export class VcfUpload {
  @Output() resultsFound = new EventEmitter<any>();
  
  selectedFile: File | null = null;
  loading: boolean = false;

  constructor(private http: HttpClient) {}

  onFileSelected(event: any) {
    const file = event.target.files[0];
    if (file && file.name.endsWith('.vcf')) {
      this.selectedFile = file;
    } else {
      alert('Please select a valid VCF file');
      this.selectedFile = null;
    }
  }

  uploadFile() {
    if (!this.selectedFile) {
      return;
    }

    this.loading = true;
    const formData = new FormData();
    formData.append('file', this.selectedFile);

    // Call your FastAPI backend
    this.http.post('http://localhost:8000/scan-vcf', formData)
      .subscribe({
        next: (response: any) => {
          console.log('Upload successful:', response);
          this.loading = false;
          this.resultsFound.emit(response);
        },
        error: (error) => {
          console.error('Upload failed:', error);
          this.loading = false;
          alert('Upload failed. Please try again.');
        }
      });
  }

  // Keep the original method for backwards compatibility
  onFileUpload(response: any) {
    console.log(response);
    this.resultsFound.emit(response);
  }
}
