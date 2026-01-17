import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VcfUpload } from './vcf-upload';

describe('VcfUpload', () => {
  let component: VcfUpload;
  let fixture: ComponentFixture<VcfUpload>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VcfUpload]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VcfUpload);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
