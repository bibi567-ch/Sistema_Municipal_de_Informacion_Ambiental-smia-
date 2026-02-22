# 🔧 Especificaciones Técnicas - SMIA

## 📋 Información General del Proyecto

| Concepto | Descripción |
|----------|-------------|
| **Nombre** | Sistema Municipal de Información Ambiental (SMIA) |
| **Problema a Resolver** | Fragmentación, desorganización y falta de integración tecnológica en la gestión de información ambiental del municipio de La Paz |
| **Objetivo Principal** | Registrar, almacenar, actualizar y gestionar información ambiental de manera integrada |
| **Presupuesto** | Bs. 208.800 |
| **Plazo de Ejecución** | 90 días |
| **Propiedad** | Todo el código y documentación generada será propiedad del GAMLP |

---

## 👥 Stakeholders Principales

| Rol | Nombre/Entidad | Nivel de Influencia | Expectativa Principal |
|-----|----------------|---------------------|----------------------|
| Cliente/Patrocinador | Secretaría Municipal de Gestión Ambiental (SMGA) | Alto | Contar con un sistema funcional, integrado y seguro |
| Cliente/Patrocinador | Swisscontact (Proyecto Basura 0) | Medio | Cumplimiento de objetivos del Proyecto "Basura 0" |
| Cliente/Patrocinador | ASDI (Agencia Sueca de Cooperación Internacional) | Medio | Uso eficiente de recursos y cumplimiento ambiental |
| Usuario Final - Interno | Técnicos Ambientales / Operadores de residuos | Alto | Plataforma fácil para cargar datos y generar reportes |
| Usuario Final - Externo | Ciudadanía del Municipio de La Paz | Medio | Acceso transparente a información ambiental |
| Equipo Técnico | Empresa Consultora (Desarrolladora) | Alto | Cumplir contrato en 90 días |
| Equipo Técnico | Supervisor Técnico (designado por SMGA) | Medio | Verificar cumplimiento de Términos de Referencia (TDR) |

---

## 🏗️ Arquitectura del Sistema
┌─────────────────────────────────────────────────────────────┐
│                    CAPA DE PRESENTACIÓN                      │
│         (Web Responsive - Móvil y Escritorio)               │
└───────────────────────┬─────────────────────────────────────┘
│
┌───────────────────────▼─────────────────────────────────────┐
│                      CAPA DE APLICACIÓN                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Login y   │  │   Gestión   │  │  Generación de      │  │
│  │   Roles     │  │   de Datos  │  │  Reportes y Mapas   │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└───────────────────────┬─────────────────────────────────────┘
│
┌───────────────────────▼─────────────────────────────────────┐
│                      CAPA DE DATOS                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Base de Datos (PostgreSQL/MySQL)            │    │
│  │   - Información histórica (mínimo 5 años)           │    │
│  │   - Puntos de monitoreo georreferenciados           │    │
│  │   - Logs de auditoría                               │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
│
┌───────────────────────▼─────────────────────────────────────┐
│                   INTEGRACIONES EXTERNAS                     │
│         SIGIR Nacional (Sistema de Gestión de Residuos)     │
└─────────────────────────────────────────────────────────────┘
---

## 💻 Stack Tecnológico

| Componente | Especificación | Restricción/Nota |
|------------|----------------|------------------|
| **Infraestructura** | Data Center GAMLP o Nube | Aprobado por el cliente |
| **Frontend** | Web Responsive (HTML5, CSS3, JavaScript) | Compatible con móvil y escritorio |
| **Backend** | Tecnología aprobada por el cliente | Cualquier tecnología previa aprobación |
| **Base de Datos** | PostgreSQL o MySQL | Soporte para datos georreferenciados |
| **Mapas** | Sistema de visualización geográfica | Visualización de puntos de monitoreo |
| **Seguridad** | Hashing de contraseñas (bcrypt/Argon2) | No texto plano |
| **Reportes** | Exportación PDF y Excel | Generación con filtros |
| **Integración** | API para SIGIR Nacional | Sincronización de datos de residuos |

---

## 🗄️ Modelos de Datos Principales
### 1. Usuarios
```sql
usuarios (
    id: INT PK,
    nombre: VARCHAR(100),
    email: VARCHAR(100) UNIQUE,
    password_hash: VARCHAR(255),  -- bcrypt/Argon2
    rol: ENUM('admin', 'tecnico', 'operador', 'ciudadano'),
    estado: BOOLEAN,
    fecha_creacion: TIMESTAMP,
    ultimo_acceso: TIMESTAMP
)

puntos_monitoreo (
    id: INT PK,
    nombre: VARCHAR(150),
    tipo: ENUM('aire', 'agua', 'residuos'),
    latitud: DECIMAL(10,8),
    longitud: DECIMAL(11,8),
    descripcion: TEXT,
    estado: BOOLEAN,
    fecha_registro: TIMESTAMP,
    usuario_registro: INT FK
)

datos_ambientales (
    id: INT PK,
    punto_id: INT FK,
    tipo_dato: VARCHAR(50),
    valor: DECIMAL(10,2),
    unidad: VARCHAR(20),
    fecha_muestreo: DATE,
    fecha_registro: TIMESTAMP,
    usuario_registro: INT FK,
    observaciones: TEXT
)

logs (
    id: INT PK,
    usuario_id: INT FK,
    accion: VARCHAR(255),
    tabla_afectada: VARCHAR(50),
    registro_id: INT,
    datos_anteriores: JSON,
    datos_nuevos: JSON,
    ip_address: VARCHAR(45),
    fecha_hora: TIMESTAMP,
    user_agent: TEXT
)

solicitudes_inspeccion (
    id: INT PK,
    numero_seguimiento: VARCHAR(20) UNIQUE,
    nombre_solicitante: VARCHAR(100),
    email: VARCHAR(100),
    descripcion: TEXT,
    ubicacion: VARCHAR(255),
    estado: ENUM('pendiente', 'en_proceso', 'atendida', 'rechazada'),
    fecha_solicitud: TIMESTAMP,
    fecha_respuesta: TIMESTAMP
)

Requisitos de Seguridad
| ID     | Requisito                        | Implementación                      |
| ------ | -------------------------------- | ----------------------------------- |
| RNF-01 | Contraseñas no en texto plano    | Hashing con bcrypt o Argon2         |
| RNF-02 | Control de acceso por roles      | Middleware de autorización          |
| RNF-03 | Bloqueo tras 3 intentos fallidos | Contador de intentos en sesión      |
| RNF-04 | Logs de auditoría                | Registro de todas las acciones CRUD |
| RNF-05 | Cumplimiento normativa TIC       | Estándares vigentes del GAMLP       |

Requisitos de Rendimiento
| ID     | Requisito                        | Métrica de Éxito                    |
| ------ | -------------------------------- | ----------------------------------- |
| RNF-02 | Tiempo de respuesta en búsquedas | < 1 segundo con 10,000 registros    |
| RNF-03 | Disponibilidad del sistema       | 24/7 operativo                      |
| RNF-04 | Carga de datos históricos        | Migración de mínimo 5 años de datos |
