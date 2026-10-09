import { Component, signal, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../../services/auth.service';
import { MonitoreoService } from '../../services/monitoreo.service';
import { MapaLeafletComponent, PuntoMapa } from '../../shared/mapa-leaflet/mapa-leaflet.component';
import { environment } from '../../../environments/environment';

interface ZonaAire { zona: string; ica: number; nivel: string; color: string; contaminante: string; actualizacion: string; }
interface AlertaActiva { tipo: string; zona: string; descripcion: string; fecha: string; icono: string; }

@Component({
  selector: 'app-portal-ciudadano',
  standalone: true,
  imports: [CommonModule, RouterLink, FormsModule, MapaLeafletComponent],
  templateUrl: './portal-ciudadano.component.html',
  styleUrls: ['./portal-ciudadano.component.css']
})
export class PortalCiudadanoComponent implements OnInit {

  authService = inject(AuthService);
  monitoreoService = inject(MonitoreoService);
  http = inject(HttpClient); // <-- Agregado para enviar las denuncias

  puntosMapa: PuntoMapa[] = [];

  // Modal de login
  mostrarLogin = signal(false);
  mostrarPassword = signal(false);
  loginEmail = '';
  loginPassword = '';
  loginError = signal('');
  loginCargando = signal(false);

  // Formulario de denuncia
  mostrarFormDenuncia = signal(false);
  denuncia = { tipo: '', descripcion: '', ubicacion: '', email_contacto: '' };
  denunciaEnviada = signal(false);
  numeroDenuncia = signal('');
  enviandoDenuncia = signal(false);

  // Datos ambientales de muestra
  zonas: ZonaAire[] = [
    { zona: 'Centro — Plaza Murillo', ica: 48, nivel: 'Bueno', color: 'green', contaminante: 'PM2.5: 12 µg/m³', actualizacion: 'Hace 15 min' },
    { zona: 'Zona Sur — Calacoto', ica: 94, nivel: 'Moderado', color: 'yellow', contaminante: 'PM10: 58 µg/m³', actualizacion: 'Hace 8 min' },
    { zona: 'Miraflores', ica: 44, nivel: 'Bueno', color: 'green', contaminante: 'PM2.5: 11 µg/m³', actualizacion: 'Hace 20 min' },
    { zona: 'Villa Fátima', ica: 118, nivel: 'Dañino grupos sensibles', color: 'orange', contaminante: 'NO₂: 78 µg/m³', actualizacion: 'Hace 5 min' },
  ];

  alertas: AlertaActiva[] = [
    { tipo: 'Calidad del Aire', zona: 'Villa Fátima', descripcion: 'ICA elevado por concentración de NO₂.', fecha: 'Hoy 08:30', icono: '💨' }
  ];

  estadisticas = { estaciones_activas: 18, denuncias_mes: 143, denuncias_resueltas: 127, rios_monitoreados: 6 };
  tiposDenuncia = ['Contaminación Aire', 'Contaminación Ríos', 'Tala Ilegal', 'Basura', 'Ruido', 'Otro'];

  ngOnInit(): void {
    this.cargarMapa();
  }

  cargarMapa(): void {
    this.monitoreoService.getPuntosMapaUnificado().subscribe({
      next: (res) => {
        this.puntosMapa = res.puntos;
      },
      error: (err) => console.error('Error al cargar el mapa:', err)
    });
  }

  getBgColor(color: string): string {
    const map: Record<string, string> = { green: 'bg-emerald-50 border-emerald-400', yellow: 'bg-amber-50 border-amber-400', orange: 'bg-orange-50 border-orange-400' };
    return map[color] ?? map['green'];
  }
  getTextColor(color: string): string {
    const map: Record<string, string> = { green: 'text-emerald-700', yellow: 'text-amber-700', orange: 'text-orange-700' };
    return map[color] ?? map['green'];
  }
  getBadgeColor(color: string): string {
    const map: Record<string, string> = { green: 'bg-emerald-500', yellow: 'bg-amber-400', orange: 'bg-orange-500' };
    return map[color] ?? map['green'];
  }

  abrirLogin(): void { this.mostrarLogin.set(true); this.loginError.set(''); this.loginEmail = ''; this.loginPassword = ''; }
  cerrarLogin(): void { this.mostrarLogin.set(false); }
  togglePassword(): void { this.mostrarPassword.update(v => !v); }

  onLogin(): void {
    if (!this.loginEmail || !this.loginPassword) { this.loginError.set('Ingresa tu correo y contraseña.'); return; }
    this.loginCargando.set(true);
    this.loginError.set('');

    this.authService.login(this.loginEmail, this.loginPassword).subscribe({
      next: (respuesta) => {
        this.loginCargando.set(false);
        this.cerrarLogin();
      },
      error: (error) => {
        this.loginCargando.set(false);
        if (error.status === 401) { this.loginError.set('Correo o contraseña incorrectos.'); } 
        else { this.loginError.set('El servidor Django está apagado. Enciéndelo.'); }
      }
    });
  }

  abrirDenuncia(): void { this.mostrarFormDenuncia.set(true); this.denunciaEnviada.set(false); }
  cerrarDenuncia(): void {
    this.mostrarFormDenuncia.set(false);
    this.denuncia = { tipo: '', descripcion: '', ubicacion: '', email_contacto: '' };
  }
  
  // AHORA SÍ ENVÍA A LA BASE DE DATOS
  onEnviarDenuncia(): void {
    if (!this.denuncia.tipo || !this.denuncia.descripcion || !this.denuncia.ubicacion) return;
    this.enviandoDenuncia.set(true);

    this.http.post<any>(`${environment.apiBaseUrl}/api/denuncias/`, this.denuncia).subscribe({
      next: (res) => {
        this.numeroDenuncia.set(res.numero_seguimiento);
        this.denunciaEnviada.set(true);
        this.enviandoDenuncia.set(false);
      },
      error: (err) => {
        console.error(err);
        alert('Ocurrió un error al enviar la denuncia. Intente de nuevo.');
        this.enviandoDenuncia.set(false);
      }
    });
  }
}