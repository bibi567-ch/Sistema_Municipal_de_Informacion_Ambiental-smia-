import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PortalCiudadanoComponent } from './portal-ciudadano.component';

describe('PortalCiudadanoComponent', () => {
  let component: PortalCiudadanoComponent;
  let fixture: ComponentFixture<PortalCiudadanoComponent>;

export class PortalCiudadanoComponent {
  titulo = 'Información Ambiental de La Paz';
  clicks = 0;                       // ← agrega esto

  contarClick(): void {              // ← agrega esto
    this.clicks++;
  }
}

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PortalCiudadanoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(PortalCiudadanoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
