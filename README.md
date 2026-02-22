# Sistema Municipal de Información Ambiental (SMIA)

## 📋 Información del Proyecto

| Concepto | Descripción |
|----------|-------------|
| **Nombre** | Sistema Municipal de Información Ambiental (SMIA) |
| **Problema a Resolver** | Fragmentación, desorganización y falta de integración tecnológica en la gestión de información ambiental del municipio de La Paz |
| **Objetivo Principal** | Registrar, almacenar, actualizar y gestionar información ambiental de manera integrada |

---

## 👥 Stakeholders (Interesados)

| Rol | Nombre/Entidad | Influencia | Expectativa Principal |
|-----|----------------|------------|----------------------|
| Cliente/Patrocinador | Secretaría Municipal de Gestión Ambiental (SMGA) | Alto | Contar con un sistema funcional, integrado y seguro |
| Cliente/Patrocinador | Swisscontact (Proyecto Basura 0) | Medio | Cumplimiento de objetivos del Proyecto "Basura 0" |
| Cliente/Patrocinador | ASDI (Agencia Sueca de Cooperación) | Medio | Uso eficiente de recursos y cumplimiento ambiental |
| Usuario Final (Interno) | Técnicos ambientales | Alto | Plataforma fácil para cargar datos y generar reportes |
| Usuario Final (Externo) | Ciudadanía de La Paz | Alto | Acceso transparente a información ambiental |
| Usuario Final (Externo) | Operadores de residuos | Medio | Registro digital y simplificación de trámites |
| Equipo Técnico | Empresa Consultora (Desarrolladora) | Alto | Cumplir contrato en 90 días |
| Equipo Técnico | Supervisor Técnico SMGA | Medio | Verificar cumplimiento de TDR |
| Equipo Técnico | Equipo de Desarrollo | Alto | Implementar solución técnica estable |

---

## ✅ Requerimientos Funcionales (RF)

| ID | Descripción | Prioridad | Criterio de Aceptación |
|----|-------------|-----------|------------------------|
| RF-01 | El sistema debe validar las credenciales de usuario (Login) | **Must** | Acceso denegado tras 3 intentos fallidos |
| RF-02 | El sistema debe permitir la asignación de roles y permisos a los usuarios | **Must** | Un usuario con rol técnico no puede acceder a funciones administrativas |
| RF-03 | El sistema debe registrar una bitácora (log) de todas las acciones realizadas en la plataforma | **Must** | Cada acción realizada queda registrada con usuario, fecha y hora |
| RF-04 | El sistema debe permitir registrar puntos de monitoreo georreferenciados (aire, agua, residuos) | **Must** | El punto se visualiza correctamente en el mapa con coordenadas guardadas |
| RF-05 | El sistema debe permitir cargar datos técnicos de monitoreo ambiental | **Must** | Los datos ingresados se almacenan correctamente en la base de datos y pueden consultarse |
| RF-06 | El sistema debe migrar información histórica de al menos 5 años a la nueva base de datos | **Must** | Los registros históricos son visibles y consultables en el sistema |
| RF-07 | El sistema debe generar reportes estadísticos por módulo ambiental | **Must** | El sistema genera reportes con filtros por fecha, área y tipo de monitoreo |
| RF-08 | El sistema debe permitir la consulta pública de información ambiental general | **Must** | Un ciudadano puede acceder sin autenticación a datos públicos |
| RF-09 | El sistema debe integrarse con el SIGIR nacional para intercambio de información de residuos | **Must** | Los datos de residuos se sincronizan con el sistema externo |
| RF-10 | El sistema debe generar mapas dinámicos con visualización de datos ambientales | **Should** | El mapa muestra filtros por tipo de monitoreo y periodo de tiempo |
| RF-11 | El sistema debe permitir exportar reportes en formato PDF o Excel | **Should** | El reporte descargado contiene los datos filtrados correctamente |
| RF-12 | El sistema debe permitir solicitudes digitales de inspección ciudadana | **Should** | La solicitud queda registrada y genera número de seguimiento |
| RF-13 | El sistema debe enviar notificaciones automáticas por correo al registrar una solicitud | **Could** | El usuario recibe un correo de confirmación tras registrar la solicitud |
| RF-14 | El sistema debe mostrar un dashboard con indicadores ambientales consolidados | **Could** | El panel muestra métricas resumidas y actualizadas |
| RF-15 | El sistema no incluirá aplicación móvil nativa en fase de proyecto | **Won't have** | La funcionalidad móvil queda documentada para futuras versiones |

---

## ⚙️ Requerimientos No Funcionales (RNF)

| ID | Categoría | Descripción | Métrica de Éxito |
|----|-----------|-------------|------------------|
| RNF-01 | Seguridad | Las contraseñas no deben guardarse en texto plano | Uso de Hashing (bcrypt/Argon2) |
| RNF-02 | Rendimiento | Tiempo de respuesta en búsquedas | Menos de 1 segundo con 10k registros |
| RNF-03 | Compatibilidad | Dispositivos soportados | Web Responsive (Móvil y Escritorio) |

---

## 📏 Reglas de Negocio y Restricciones

- **Presupuesto máximo:** Bs. 208.800
- **Plazo de ejecución:** 90 días
- **Tecnología:** Cualquier tecnología aprobada
- **Infraestructura:** Data Center del GAMLP o en la nube
- **Migración:** Mínimo 5 años de información histórica
- **Integración:** Con sistema nacional SIGIR
- **Normativa:** Debe cumplir la normativa TIC vigente
- **Propiedad:** Toda la información y código generado serán propiedad del GAMLP

---

## ✔️ Checklist de Validación

- [x] ¿Son los requerimientos claros y sin ambigüedades?
- [x] ¿Son los requerimientos medibles (se pueden probar)?
- [x] ¿Todos los stakeholders clave han aprobado esta lista?
- [x] ¿Se han identificado riesgos técnicos asociados a los requerimientos complejos?

---

**Fecha de documento:** 19/02/2026  
**Autores:** Génesis Sarai Apaza Quispe, Esmeralda Alegre Mamani, Anel Kahori Quiroz Crespo, Eva Lizeth Chino Quispe, Daynor Juan Mamani Condori
