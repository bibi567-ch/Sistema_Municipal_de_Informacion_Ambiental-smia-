# 🌿 Sistema Municipal de Información Ambiental (SMIA - GAMLP)

El **SMIA** es una plataforma integral diseñada para el Gobierno Autónomo Municipal de La Paz (GAMLP). Su objetivo es centralizar, gestionar y transparentar la información ambiental, eliminando la fragmentación de datos de aire, agua y residuos.

---

##  Resumen Ejecutivo

* **Problema:** Dispersión de datos ambientales y falta de reportes consolidados.
* **Solución:** Plataforma web centralizada con visor GIS y sincronización nacional.
* **Impacto:** Mejora en la toma de decisiones para la Secretaría Municipal de Gestión Ambiental (SMGA).

---

##  Arquitectura Funcional (Diagrama de Casos de Uso)

El sistema se estructura en 4 módulos principales que interactúan con actores internos (Técnicos/Administradores) y externos (Ciudadanía y Sistemas Nacionales).

### 📊 Diagrama de Casos de Uso
![Diagrama de Casos de Uso](smia_Diagrama).png

###  Desglose de Operaciones por Actor
| Actor | Responsabilidades Clave |
| :--- | :--- |
| **Administrador** | Gestión de usuarios (RBAC), Auditoría de logs (RF-03). |
| **Técnico Ambiental** | Carga de datos técnicos (RF-05), Gestión de capas GIS (RF-10). |
| **Ciudadano** | Consultas públicas (RF-08), Solicitud de inspecciones (RF-12). |
| **Sistemas Externos** | Sincronización con **SIGIR**, **Red MONICA** y **Línea 155**. |

---

##  Especificaciones Técnicas (RF & RNF)

### Requerimientos Críticos (Prioridad: Must)
- **Seguridad:** Autenticación robusta y bloqueo de seguridad (RF-01).
- **Georreferenciación:** Puntos de monitoreo con coordenadas precisas (RF-04).
- **Interoperabilidad:** Integración mediante API con el sistema nacional SIGIR (RF-09).
- **Migración:** Tratamiento de 5 años de datos históricos (RF-06).

### Atributos de Calidad (No Funcionales)
- **Rendimiento:** Consultas optimizadas para responder en < 1s (RNF-02).
- **Seguridad de Datos:** Hashing de contraseñas con `bcrypt` (RNF-01).
- **UX/UI:** Diseño responsivo para tablets de campo y monitores de oficina.

---

##  Guía de Desarrollo (Angular)

### Requisitos Previos
* Node.js v18+
* Angular CLI 18.2.21

### Instalación y Ejecución
1.  Clonar repositorio: `git clone https://github.com/tu-usuario/smia-gamlp.git`
2.  Instalar dependencias: `npm install`
3.  Lanzar servidor local: `ng serve`
4.  Navegar a: `http://localhost:4200/`

---

## 👥 Equipo de Proyecto
* **Génesis Sarai Apaza Quispe** - *Analista de Sistemas*
* **Esmeralda Alegre Mamani** - *Desarrolladora Frontend*
* **Anel Kahori Quiroz Crespo** - *Especialista en QA*
* **Eva Lizeth Chino Quispe** - *Diseñadora UI/UX*
* **Daynor Juan Mamani Condori** - *Administrador de Base de Datos*

---
