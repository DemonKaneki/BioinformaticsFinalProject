import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MutationList } from './mutation-list';

describe('MutationList', () => {
  let component: MutationList;
  let fixture: ComponentFixture<MutationList>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MutationList]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MutationList);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
