# **Blueprint Arquitectónico: Proyecto SMIA**

**Ecosistema Desacoplado: Frontend (Angular) \+ Backend (API REST con Django)**

## **1\. Visión General de la Arquitectura**

El Sistema Municipal de Información Ambiental (SMIA) utilizará una arquitectura **Cliente-Servidor Desacoplada**.

Esto significa que el sistema se divide en dos aplicaciones completamente independientes que se comunican entre sí a través de internet usando el formato JSON.

1. **Frontend (App Cliente):** Se ejecutará en el navegador del ciudadano o del inspector. Será una **SPA (Single Page Application)** y una **PWA (Progressive Web App)** para permitir el trabajo *offline* en zonas sin cobertura.  
2. **Backend (Servidor API):** Vivirá en los servidores del GAMLP. Recibirá las peticiones, aplicará las reglas de negocio, procesará las coordenadas geográficas y consultará la base de datos.  
3. **Base de Datos:** Estará oculta y protegida, accesible únicamente por el Backend.

## **2\. CAPA FRONTEND (La Interfaz de Usuario)**

### **Tecnologías a Utilizar:**

* **Framework Core:** Angular 17+ (Usando *Standalone Components* para mayor velocidad y menor código).  
* **Estilos y UI:** Tailwind CSS (Permite un diseño *responsive* muy rápido, vital para que los inspectores lo usen en tablets/móviles).  
* **Mapas:** Leaflet.js (Librería open-source para renderizar los mapas de contaminación y denuncias).  
* **Almacenamiento Offline:** IndexedDB (Integrado mediante Service Workers de Angular para guardar denuncias sin internet y sincronizarlas después).

### **Patrones de Diseño (Frontend):**

* **Observer (Observador):** Usando RxJS. Angular reaccionará automáticamente a los cambios. Si un inspector sube una foto, la barra de carga se actualizará reactivamente.  
* **Facade (Fachada):** Los componentes visuales (HTML) no harán llamadas HTTP directas. Llamarán a un "Servicio Fachada" que ocultará la complejidad de consultar la API.  
* **Singleton:** Los servicios globales (como el AuthService que guarda el Token JWT del usuario) tendrán una única instancia en toda la aplicación.

### **Estructura de Carpetas (Feature-Driven Development):**

Angular se organizará por funcionalidades, no por tipos de archivo. Esto hace que el proyecto sea infinitamente escalable.

smia-frontend-angular/  
├── src/  
│   ├── app/  
│   │   ├── core/                  \# Carga inicial (Esqueleto)  
│   │   │   ├── guards/            \# Rutas protegidas (Ej: auth.guard.ts)  
│   │   │   ├── interceptors/      \# Inyecta el Token en cada petición HTTP  
│   │   │   ├── layout/            \# Navbar, Sidebar institucional, Footer  
│   │   │   └── services/          \# Servicios HTTP globales (API externas)  
│   │   │  
│   │   ├── shared/                \# Componentes que se reusan en toda la app  
│   │   │   ├── components/        \# Modales, Botones, Visor de Mapas (Leaflet)  
│   │   │   ├── pipes/             \# Filtros de fecha, moneda, coordenadas  
│   │   │   └── models/            \# Interfaces TypeScript (Ej: denuncia.model.ts)  
│   │   │  
│   │   ├── features/              \# MÓDULOS DE NEGOCIO (El corazón del SMIA)  
│   │   │   ├── auth/              \# Login conectado al LDAP/AD del GAMLP  
│   │   │   ├── portal-ciudadano/  \# Vista pública, semáforo ICA  
│   │   │   ├── inspecciones/      \# Módulo para técnicos (soporta Offline)  
│   │   │   ├── reportes/          \# Gráficos y estadísticas  
│   │   │   └── residuos/          \# Módulo Ley 755 e integración SIGIR  
│   │   │  
│   │   ├── app.component.ts       \# Componente raíz  
│   │   ├── app.routes.ts          \# Enrutador principal  
│   │   └── app.config.ts          \# Configuración de Angular 17+  
│   │  
│   ├── assets/                    \# Logos del GAMLP, iconos, fuentes  
│   └── styles.css                 \# Importación de Tailwind CSS

## **3\. CAPA BACKEND (La Lógica de Negocio y API REST)**

### **Tecnologías a Utilizar:**

* **Lenguaje y Framework:** Python 3 \+ Django.  
* **API Framework:** Django REST Framework (DRF). Es robusto, seguro y permite crear APIs rápidamente.  
* **Geoprocesamiento:** GeoDjango. Dado que el SMIA maneja estaciones de la *Red MoniCA*, ríos y ubicaciones de denuncias, GeoDjango es fundamental para calcular distancias, áreas afectadas e intersecciones espaciales.  
* **Autenticación:** JWT (JSON Web Tokens) e integración con LDAP (Active Directory) del municipio.

### **Patrones de Diseño (Backend):**

* **MVT / MVC (Model-View-Template/Controller):** Separación estricta entre Modelos (BD), Vistas (Lógica/Endpoints) y Serializadores (Formateadores de JSON).  
* **DTO (Data Transfer Object):** Implementado a través de los *Serializers* de Django REST. Filtran y formatean qué datos de la base de datos se exponen de forma segura a Angular.  
* **Repository Pattern (Adaptado):** El ORM de Django actúa como repositorio, aislando las consultas complejas de PostGIS de la lógica de los endpoints.

### **Estructura de Carpetas (Domain-Driven Design en Django):**

Django separa el código en pequeñas aplicaciones ("apps") reutilizables.

smia-backend-django/  
├── smia\_core/                     \# Configuración principal del proyecto  
│   ├── settings.py                \# Configuración de BD, JWT, GeoDjango  
│   ├── urls.py                    \# Enrutador de la API (Endpoint maestro)  
│   └── wsgi.py / asgi.py          \# Archivos de despliegue en servidor  
│  
├── apps/                          \# Sub-módulos del sistema (Dominios)  
│   ├── accounts/                  \# Gestión de Usuarios y Roles (Inspectores, Admin)  
│   │   ├── models.py              \# Extensión del usuario por defecto  
│   │   └── views.py               \# Lógica de Login/LDAP  
│   │  
│   ├── medio\_ambiente/            \# Lógica de Aire, Agua, Ruido  
│   │   ├── models.py              \# Tablas de Estaciones, Muestras, Parámetros  
│   │   ├── serializers.py         \# Formatea los datos a JSON para Angular  
│   │   ├── views.py               \# Endpoints REST (GET, POST, PUT, DELETE)  
│   │   └── gis\_utils.py           \# Lógica geoespacial compleja  
│   │  
│   ├── denuncias/                 \# Atención a incidentes ciudadanos  
│   │   ├── models.py              \# Datos de denuncia (incuye campo de polígono/punto)  
│   │   └── views.py               \# Lógica de estados (Borrador \-\> Aprobada)  
│   │  
│   └── sigir\_integration/         \# Orquestador para comunicación con Ministerio  
│       └── api\_client.py          \# Funciones que envían datos al sistema nacional  
│  
├── requirements.txt               \# Librerías de Python  
└── manage.py                      \# Orquestador de consola

## **4\. BASE DE DATOS Y DEVOPS (Infraestructura)**

* **Base de Datos:** PostgreSQL con la extensión PostGIS. PostGIS convierte a PostgreSQL en una base de datos espacial, permitiendo guardar geometrías (puntos, líneas, polígonos) en lugar de solo texto y números.  
* **DevOps (Despliegue):** Docker y Docker Compose.  
  * Se creará un docker-compose.yml que levantará 3 contenedores:  
    1. Contenedor de Node/Nginx sirviendo **Angular**.  
    2. Contenedor de Python/Gunicorn sirviendo **Django**.  
    3. Contenedor de **PostgreSQL/PostGIS**.  
  * *Ventaja:* Garantiza que si el sistema funciona en la computadora de los desarrolladores, funcionará exactamente igual en los servidores del GAMLP.
