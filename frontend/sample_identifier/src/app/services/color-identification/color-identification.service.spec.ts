import { TestBed } from '@angular/core/testing';

import { ColorIdentificationService } from './color-identification.service';

describe('ColorIdentificationService', () => {
  let service: ColorIdentificationService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ColorIdentificationService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
