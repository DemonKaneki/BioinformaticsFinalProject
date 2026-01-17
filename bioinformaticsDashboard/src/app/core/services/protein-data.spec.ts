import { TestBed } from '@angular/core/testing';

import { ProteinData } from './protein-data';

describe('ProteinData', () => {
  let service: ProteinData;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProteinData);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
