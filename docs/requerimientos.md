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
