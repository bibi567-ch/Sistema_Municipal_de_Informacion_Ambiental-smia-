import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="animate-in fade-in slide-in-from-bottom-4 duration-700">
      <div class="bg-gradient-to-r from-uab-green to-emerald-900 rounded-3xl p-10 text-white shadow-2xl relative overflow-hidden mb-10">
        <div class="relative z-10">
          <h1 class="text-4xl font-black mb-2">¡Bienvenido al Ecosistema SMIA!</h1>
          <p class="text-emerald-100 text-lg max-w-xl font-light">Estructura base desplegada con éxito. Cada integrante ahora puede crear su módulo en su propia carpeta sin generar conflictos en el núcleo del sistema.</p>
        </div>
        <i class="fas fa-shield-alt absolute -right-10 -bottom-10 text-[200px] opacity-10 rotate-12"></i>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-8 rounded-3xl shadow-sm border border-slate-200 hover:shadow-xl transition-shadow group">
          <div class="w-14 h-14 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-blue-600 group-hover:text-white transition-colors">
            <i class="fas fa-layer-group text-2xl"></i>
          </div>
          <h3 class="text-xl font-bold mb-3 text-slate-800">Clean Arch</h3>
          <p class="text-slate-500 text-sm leading-relaxed">Arquitectura desacoplada. El núcleo (Core) está separado de los módulos específicos (Features).</p>
        </div>

        <div class="bg-white p-8 rounded-3xl shadow-sm border border-slate-200 hover:shadow-xl transition-shadow group">
          <div class="w-14 h-14 bg-emerald-50 text-emerald-600 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-emerald-600 group-hover:text-white transition-colors">
            <i class="fas fa-code-branch text-2xl"></i>
          </div>
          <h3 class="text-xl font-bold mb-3 text-slate-800">Branch Flow</h3>
          <p class="text-slate-500 text-sm leading-relaxed">Uso obligatorio de ramas <code>feature/</code>. Pull Requests revisados por pares para nivel experto.</p>
        </div>

        <div class="bg-white p-8 rounded-3xl shadow-sm border border-slate-200 hover:shadow-xl transition-shadow group">
          <div class="w-14 h-14 bg-amber-50 text-amber-600 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-amber-600 group-hover:text-white transition-colors">
            <i class="fas fa-bolt text-2xl"></i>
          </div>
          <h3 class="text-xl font-bold mb-3 text-slate-800">Tailwind Engine</h3>
          <p class="text-slate-500 text-sm leading-relaxed">Estilos encapsulados por componente. Cero conflictos de CSS entre compañeros de equipo.</p>
        </div>
      </div>
    </div>
  `
})
export class DashboardComponent {}
