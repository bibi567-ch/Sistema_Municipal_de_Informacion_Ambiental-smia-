import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <div class="flex h-screen overflow-hidden bg-slate-50 font-sans text-slate-900">

      <aside class="w-72 bg-uab-green text-white flex flex-col shadow-2xl z-20">

        <div class="h-20 flex items-center px-8 border-b border-white/10 bg-black/10">
          <i class="fas fa-leaf text-2xl mr-3 text-emerald-400"></i>
          <span class="text-2xl font-black tracking-tighter uppercase">SMIA <span class="font-light text-emerald-400">UAB</span></span>
        </div>

        <nav class="flex-1 overflow-y-auto py-6 px-4 space-y-1">
          <div class="px-4 text-[10px] font-bold text-emerald-500 uppercase tracking-[0.2em] mb-4">Menú Principal</div>

          <a routerLink="/dashboard" routerLinkActive="bg-white/10 text-emerald-400 ring-1 ring-white/20"
             class="flex items-center px-4 py-3 rounded-xl transition-all hover:bg-white/5 group">
            <i class="fas fa-th-large w-6 text-lg group-hover:scale-110 transition-transform"></i>
            <span class="ml-3 font-medium">Dashboard General</span>
          </a>

          <div class="px-4 text-[10px] font-bold text-emerald-500 uppercase tracking-[0.2em] mt-8 mb-4">Gestión Ambiental</div>

          <a class="flex items-center px-4 py-3 rounded-xl opacity-50 cursor-not-allowed">
            <i class="fas fa-wind w-6 text-lg text-slate-400"></i>
            <span class="ml-3 font-medium">Calidad del Aire</span>
          </a>

          <a routerLink="/agua" routerLinkActive="bg-white/10 text-emerald-400 ring-1 ring-white/20"
            class="flex items-center px-4 py-3 rounded-xl transition-all hover:bg-white/5 group">
            <i class="fas fa-tint w-6 text-lg group-hover:scale-110 transition-transform"></i>
            <span class="ml-3 font-medium">Calidad Hídrica</span>
          </a>
        </nav>

        <div class="p-6 border-t border-white/10 bg-black/10 flex items-center">
          <div class="w-12 h-12 rounded-2xl bg-emerald-500 flex items-center justify-center font-black text-uab-green shadow-lg ring-4 ring-emerald-500/20">
            DM
          </div>
          <div class="ml-4">
            <p class="text-sm font-bold leading-none">Daynor Mamani</p>
            <p class="text-[10px] text-emerald-400 mt-1 uppercase font-bold tracking-widest">Tech Lead / SM</p>
          </div>
        </div>
      </aside>

      <div class="flex-1 flex flex-col relative overflow-hidden">

        <header class="h-20 bg-white border-b border-slate-200 flex items-center justify-between px-10">
          <div>
            <h2 class="text-sm font-bold text-slate-400 uppercase tracking-widest">Sistema Municipal de Información Ambiental</h2>
            <p class="text-xs text-slate-500 font-medium">La Paz - Proyecto "Basura 0"</p>
          </div>
          <div class="flex items-center gap-4">
            <button class="w-10 h-10 rounded-full bg-slate-100 text-slate-500 hover:bg-emerald-50 hover:text-emerald-600 transition-colors flex items-center justify-center">
              <i class="fas fa-bell"></i>
            </button>
          </div>
        </header>

        <main class="flex-1 overflow-y-auto p-10">
          <router-outlet></router-outlet>
        </main>
      </div>

    </div>
  `
})
export class LayoutComponent {}
