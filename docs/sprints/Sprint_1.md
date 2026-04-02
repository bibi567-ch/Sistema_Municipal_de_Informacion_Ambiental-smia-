# SPRINT 1 – Autenticación, roles, auditoría, CI/CD y Docker

## Sprint Planning

**Fecha:** 01/04/2026
**Duración:** 7 días

### Objetivo:

Implementar autenticación básica del sistema.

### Historias:

* HU-01.1 Login
* HU-01.2 Registro
* HU-01.1 Login
* HU-01.2 Registro
* HU-02.1 Crear Proyecto
* HU-02.2 Ver Proyectos
* HU-03.1 Clasificación TRL con IA
* RNF-01 Seguridad de Datos
* DEV-01 Configuración del Proyecto
* DEV-02 Implementación Backend y Base de Datos
* DEV-03 Integración de Inteligencia Artificial  

---

## Distribución de tareas

### 👩‍💻 Backend (Eva)
Descripción: Desarrollo del backend y lógica de IA

Subtareas:
- Configurar proyecto (FastAPI / Firebase Functions)
- Implementar endpoint /login
- Integrar API de Gemini
- Crear lógica de clasificación TRL
- Manejar autenticación JWT

---

### 👨‍💻 Base de Datos (Anel)
Descripción: Diseño y gestión de datos en Firebase

Subtareas:
- Crear colección usuarios
- Crear colección proyectos
- Definir estructura JSON (desde prompts)
- Configurar reglas de seguridad (Firestore)
- Validar relaciones de datos

---

### 👩‍💻 Frontend (Esmeralda)
Descripción: Desarrollo de interfaz de usuario

Subtareas:
- Crear formulario login
- Crear formulario registro
- Diseñar dashboard (Tailwind)
- Integrar botón “Analizar con IA”
- Validaciones de formulario

---

### 👨‍💻 DevOps (Daynor)
Descripción: Infraestructura y despliegue

Subtareas:
- Crear repositorio en GitHub
- Configurar Docker
- Configurar CI/CD
- Desplegar en Firebase Hosting
- Automatizar builds

---

### 👩‍💼 QA (Génesis)
Descripción: Validación y documentación

Subtareas:
- Probar login
- Validar clasificación IA
- Detectar errores
- Documentar funcionalidades
- Registrar pruebas
## Daily Scrum 1

**Fecha:** 02/04/2026

* Backend: inició API
* BD: diseño tablas
* Frontend: diseño UI
* DevOps: repo creado
* QA: revisión

**Bloqueos:** ninguno

---

## Daily Scrum 2

**Fecha:** 06/04/2026

* Backend: endpoint login
* BD: tabla creada
* Frontend: formulario listo
* DevOps: Docker
* QA: pruebas

**Bloqueos:** conexión BD

---

## Sprint Review

Login funcionando correctamente.

---

## Retrospectiva

✔ Bien: trabajo en equipo
⚠ Mejorar: comunicación

**Acción:** reuniones más claras
