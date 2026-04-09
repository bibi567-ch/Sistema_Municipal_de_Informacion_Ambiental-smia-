import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-agua',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="animate-in fade-in duration-700">
      <div class="flex flex-col md:flex-row md:items-center justify-between mb-10 gap-4">
        <div>
          <h2 class="text-3xl font-black text-slate-800 tracking-tight">Calidad Hídrica</h2>
          <p class="text-slate-500 font-medium italic">Monitoreo de cuencas y ríos - Municipio de La Paz</p>
        </div>
        <div class="flex gap-3">
          <button class="bg-white border border-slate-200 text-slate-700 px-5 py-2.5 rounded-2xl shadow-sm hover:bg-slate-50 transition-all font-bold text-sm">
            <i class="fas fa-file-export mr-2 text-blue-500"></i> Exportar
          </button>
          <button class="bg-blue-600 text-white px-6 py-2.5 rounded-2xl shadow-lg shadow-blue-200 hover:bg-blue-700 transition-all font-bold text-sm">
            <i class="fas fa-plus-circle mr-2"></i> Nuevo Registro
          </button>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-12">
        <div class="bg-white p-6 rounded-[2rem] border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
          <p class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.2em] mb-2">pH Promedio</p>
          <p class="text-3xl font-black text-blue-600">7.2 <span class="text-xs font-bold text-emerald-500 ml-1">ÓPTIMO</span></p>
        </div>
        <div class="bg-white p-6 rounded-[2rem] border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
          <p class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.2em] mb-2">Turbidez (NTU)</p>
          <p class="text-3xl font-black text-blue-600">4.1 <span class="text-xs font-normal text-slate-400 ml-1">Normal</span></p>
        </div>
        <div class="bg-white p-6 rounded-[2rem] border border-slate-100 shadow-sm hover:shadow-md transition-shadow">
          <p class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.2em] mb-2">Oxígeno Dis.</p>
          <p class="text-3xl font-black text-emerald-500">8.4 <span class="text-xs font-normal text-slate-400 ml-1">mg/L</span></p>
        </div>
        <div class="bg-white p-6 rounded-[2rem] border border-slate-100 shadow-sm hover:shadow-md transition-shadow border-l-4 border-l-red-500">
          <p class="text-[10px] font-bold text-red-400 uppercase tracking-[0.2em] mb-2">Puntos Críticos</p>
          <p class="text-3xl font-black text-red-600">03 <span class="text-xs font-normal text-slate-400 ml-1">Choqueyapu</span></p>
        </div>
      </div>

      <div class="bg-white rounded-[2.5rem] shadow-sm border border-slate-100 overflow-hidden">
        <div class="p-8 border-b border-slate-50 flex items-center justify-between bg-slate-50/30">
          <h3 class="font-bold text-slate-800">Registros Recientes de Laboratorio</h3>
          <span class="text-[10px] bg-blue-100 text-blue-700 px-4 py-1.5 rounded-full font-black uppercase tracking-widest">En línea</span>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left">
            <thead>
              <tr class="text-slate-400 text-[10px] uppercase tracking-[0.15em] border-b border-slate-100">
                <th class="px-8 py-5 font-black">Estación de Muestreo</th>
                <th class="px-8 py-5 font-black">Fecha/Hora</th>
                <th class="px-8 py-5 font-black">pH</th>
                <th class="px-8 py-5 font-black">Estado Norma</th>
                <th class="px-8 py-5 font-black text-right">Acciones</th>
              </tr>
            </thead>
            <tbody class="text-sm">
              <tr class="border-b border-slate-50 hover:bg-blue-50/30 transition-colors group">
                <td class="px-8 py-6">
                  <div class="font-bold text-slate-700">Puente Minasa</div>
                  <div class="text-[10px] text-slate-400">Cuenca Irpavi</div>
                </td>
                <td class="px-8 py-6 text-slate-500 font-medium">12/04/2026 - 09:15</td>
                <td class="px-8 py-6 font-mono font-bold text-blue-600 text-lg">7.1</td>
                <td class="px-8 py-6">
                  <span class="bg-emerald-100 text-emerald-700 px-3 py-1 rounded-lg text-[10px] font-black uppercase ring-1 ring-emerald-200">Cumple Ley 1333</span>
                </td>
                <td class="px-8 py-6 text-right">
                  <button class="text-slate-300 group-hover:text-blue-600 transition-colors"><i class="fas fa-ellipsis-h"></i></button>
                </td>
              </tr>
              <tr class="border-b border-slate-50 hover:bg-blue-50/30 transition-colors group">
                <td class="px-8 py-6">
                  <div class="font-bold text-slate-700">Río Choqueyapu (Centro)</div>
                  <div class="text-[10px] text-slate-400">Z. Central</div>
                </td>
                <td class="px-8 py-6 text-slate-500 font-medium">11/04/2026 - 15:30</td>
                <td class="px-8 py-6 font-mono font-bold text-red-500 text-lg">4.2</td>
                <td class="px-8 py-6">
                  <span class="bg-red-100 text-red-700 px-3 py-1 rounded-lg text-[10px] font-black uppercase ring-1 ring-red-200">No Cumple</span>
                </td>
                <td class="px-8 py-6 text-right">
                  <button class="text-slate-300 group-hover:text-blue-600 transition-colors"><i class="fas fa-ellipsis-h"></i></button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  `
})
export class AguaComponent {}
