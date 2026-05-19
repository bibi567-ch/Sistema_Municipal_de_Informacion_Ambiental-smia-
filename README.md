# 🌿 Sistema Municipal de Información Ambiental (SMIA - GAMLP)

![Angular](https://img.shields.io/badge/Frontend-Angular_17+-dd0031?style=for-the-badge&logo=angular)
![Django](https://img.shields.io/badge/Backend-Django_REST-092E20?style=for-the-badge&logo=django)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL_PostGIS-336791?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/DevOps-Docker_Compose-2496ED?style=for-the-badge&logo=docker)
![Estado](https://img.shields.io/badge/Estado-En_Desarrollo-brightgreen?style=for-the-badge)

El **SMIA** es una plataforma integral diseñada para el Gobierno Autónomo Municipal de La Paz (GAMLP). Su objetivo es centralizar, gestionar y transparentar la información ambiental, eliminando la fragmentación de datos de aire, agua y residuos en el marco del Proyecto "Basura 0".

---

## 📋 Resumen Ejecutivo

* **Problema:** Dispersión de datos ambientales en hojas de cálculo y falta de reportes consolidados para el Ministerio de Medio Ambiente y Agua (MMAyA).
* **Solución:** Plataforma web centralizada con visor GIS, geoprocesamiento y sincronización nacional.
* **Impacto:** Mejora en la toma de decisiones para la Secretaría Municipal de Gestión Ambiental (SMGA) y cumplimiento de normativas (Ley N°755, Ley N°1333).

---

## 🏗️ Arquitectura del Sistema

El sistema utiliza una arquitectura **Cliente-Servidor Desacoplada**:

1. **Capa Frontend (SPA):** Desarrollada en **Angular 17+** con **Tailwind CSS** para un diseño responsivo. Integración de **Leaflet.js** para renderizar mapas de contaminación y denuncias.
2. **Capa Backend (API REST):** Construida con **Python 3 y Django REST Framework**. Maneja la lógica de negocio, autenticación JWT e integración con el Active Directory del municipio.
3. **Base de Datos Espacial:** **PostgreSQL con PostGIS** para geoprocesamiento avanzado (cálculo de distancias, áreas afectadas e intersecciones espaciales).
4. **DevOps:** Contenerización completa con **Docker y Docker Compose** para garantizar despliegues idénticos en entornos de desarrollo, staging y producción.

---

## 🎨 Diseño UI/UX y Prototipos

Como parte del desarrollo centrado en el usuario (ciudadanos y técnicos de campo), se han diseñado interfaces de alta fidelidad:
* 🔐 [Mockup de Autenticación Segura (JWT)](https://www.figma.com/make/tKBYxgLWHbF4HgmaEIKjuD/Secure-Login-with-JWT?t=kML16D12bqdJgUJx-20&fullscreen=1&preview-route=%2Fdashboard)
* 📊 [Mockup de Generación de Reportes](https://www.figma.com/make/JyabLSV7yYMC06s2rfGVih/Generar-reportes-de-calidad?t=2iQ4JZxE2z1OOko8-20&fullscreen=1)
* 🌍 [Mockup de Consulta Pública Ambiental](https://www.figma.com/make/q9aZzew39qF7jf3B6kuWUk/Consulta-de-informaci%C3%B3n-ambiental?t=blDQs7fJ4NUN8uid-20&fullscreen=1)

---

## ⚙️ Especificaciones Técnicas (RF & RNF)

### Requerimientos Críticos (Must Have)
- **Seguridad:** Autenticación robusta con JWT, hashing de contraseñas (`bcrypt`/`Argon2id`) y bloqueo de seguridad (RF-01, RNF-01).
- **Georreferenciación:** Registro de puntos de monitoreo de aire, agua, ruido y residuos con coordenadas precisas (RF-04).
- **Interoperabilidad:** Integración automática mediante API con el sistema nacional SIGIR (RF-09).
- **Auditoría:** Registro inalterable de bitácora de acciones del sistema (RF-03).

### Atributos de Calidad
- **Rendimiento:** Consultas optimizadas para responder en < 1s incluso con más de 10,000 registros (RNF-02).
- **UX/UI:** Diseño responsivo (Mobile-First) garantizado para operabilidad en tablets de campo de los técnicos (RNF-03).

---

## 🗺️ Diagrama de Casos de Uso y Actores

![Diagrama de Casos de Uso](https://raw.githubusercontent.com/bibi567-ch/Sistema_Municipal_de_Informacion_Ambiental-smia-/main/smia_Diagrama.png)

| Actor | Responsabilidades Clave |
| :--- | :--- |
| **Administrador** | Gestión de usuarios (RBAC), Auditoría de logs, asignación de roles. |
| **Técnico Ambiental** | Carga de datos técnicos (ICA, parámetros hídricos), Gestión de capas GIS. |
| **Ciudadano** | Consultas públicas en mapa unificado, Solicitud ciudadana de inspecciones. |
| **Sistemas Externos** | Sincronización automática con **SIGIR MMAyA** (Ley N°755). |

---

## 🚀 Guía de Desarrollo (Frontend)

### Requisitos Previos
* Node.js v18+
* Angular CLI 18.2.21

### Instalación y Ejecución Local
```bash
# 1. Clonar repositorio
git clone [https://github.com/bibi567-ch/Sistema_Municipal_de_Informacion_Ambiental-smia-.git](https://github.com/bibi567-ch/Sistema_Municipal_de_Informacion_Ambiental-smia-.git)

# 2. Instalar dependencias
npm install

# 3. Lanzar servidor local
ng serve
