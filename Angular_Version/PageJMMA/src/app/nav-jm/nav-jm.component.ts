import { Component } from '@angular/core';
import { BreakpointObserver, Breakpoints, BreakpointState } from '@angular/cdk/layout';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { pagesJM } from 'src/assets/objects/pagesJM';

@Component({
  selector: 'nav-jm',
  templateUrl: './nav-jm.component.html',
  styleUrls: ['./nav-jm.component.scss']
})
export class NavJMComponent {

  public pagesJM = pagesJM;

  isHandset$: Observable<boolean> = this.breakpointObserver.observe(Breakpoints.Handset)
    .pipe(
      map(result => result.matches)
    );

  constructor(private breakpointObserver: BreakpointObserver) {
  }


}
