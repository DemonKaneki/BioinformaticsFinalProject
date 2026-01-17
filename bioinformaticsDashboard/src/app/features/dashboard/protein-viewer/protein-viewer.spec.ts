import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProteinViewer } from './protein-viewer';

describe('ProteinViewer', () => {
  let component: ProteinViewer;
  let fixture: ComponentFixture<ProteinViewer>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProteinViewer]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProteinViewer);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
