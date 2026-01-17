import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NeuralAnimation } from './neural-animation';

describe('NeuralAnimation', () => {
  let component: NeuralAnimation;
  let fixture: ComponentFixture<NeuralAnimation>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NeuralAnimation]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NeuralAnimation);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
