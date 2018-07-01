
import { fakeAsync, ComponentFixture, TestBed } from '@angular/core/testing';

import { NavJMComponent } from './nav-jm.component';

describe('NavJMComponent', () => {
  let component: NavJMComponent;
  let fixture: ComponentFixture<NavJMComponent>;

  beforeEach(fakeAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ NavJMComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NavJMComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should compile', () => {
    expect(component).toBeTruthy();
  });
});
