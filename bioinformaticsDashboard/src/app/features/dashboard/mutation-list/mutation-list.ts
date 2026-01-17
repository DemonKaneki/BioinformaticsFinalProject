import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-mutation-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './mutation-list.html',
  styleUrl: './mutation-list.css',
})
export class MutationList {
  @Input() mutations: any[] = [];
  @Output() selected = new EventEmitter<any>();
  
  selectedItem: any = null;

  onSelect(mutation: any) {
    this.selectedItem = mutation;
    this.selected.emit(mutation);
  }

  // Keep the original method for backwards compatibility
  onMutationClick(mutation: any) {
    this.onSelect(mutation);
  }
}
