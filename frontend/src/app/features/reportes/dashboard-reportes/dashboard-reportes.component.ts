import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-dashboard-reportes',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './dashboard-reportes.component.html',
  styles: [`
    @media print {
      .no-print { display: none !important; }
      .print-exact { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
    }
  `]
})
export class DashboardReportesComponent {
  fechaActual = new Date().toLocaleDateString('es-BO', { year: 'numeric', month: 'long', day: 'numeric' });

  imprimirPDF(): void {
    window.print();
  }
}