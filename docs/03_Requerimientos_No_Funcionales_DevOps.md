# 03_Requerimientos_No_Funcionales_DevOps

| ID | Requerimiento | Prioridad | Criterios de Aceptación |
|----|--------------|----------|--------------------------|
| RF-01 | Autenticación segura con OAuth2/JWT | Alta | El usuario puede iniciar sesión; se genera token válido; se bloquea tras 3 intentos fallidos |
| RF-02 | Gestión de roles y permisos | Alta | El administrador puede asignar roles; los usuarios solo acceden a funciones permitidas |
| RF-03 | Registro de bitácora (logs) | Media | Se registran acciones con usuario, fecha y hora; el auditor puede consultarlas |
| RF-04 | Registro de puntos georreferenciados | Alta | Se pueden registrar coordenadas; los puntos se almacenan correctamente |
| RF-05 | Carga de datos técnicos ambientales | Alta | Los técnicos ingresan datos; el sistema los valida y guarda correctamente |
| RF-06 | Migración de datos históricos | Media | Se cargan datos de al menos 5 años; se pueden consultar sin errores |
| RF-07 | Generación de reportes | Alta | Se generan reportes filtrados por módulo; los datos son correctos |
| RF-08 | Consulta pública | Alta | El ciudadano puede acceder sin login; la información es visible |
| RF-09 | Integración con SIGIR | Media | Se sincronizan datos correctamente con el sistema externo |
| RF-10 | Mapas dinámicos con filtros | Alta | El usuario puede filtrar por contaminante y periodo; el mapa se actualiza |
| RF-11 | Exportación de reportes | Alta | Se exportan reportes en PDF/Excel sin errores |
| RF-12 | Solicitudes de inspección | Media | El ciudadano puede registrar solicitudes; se almacenan correctamente |
| RF-13 | Notificaciones por correo | Media | El usuario recibe notificaciones ante eventos del sistema |
| RF-14 | Dashboard ambiental | Alta | Se visualizan indicadores claros y actualizados |
| RF-15 | Compresión de imágenes | Baja | Las imágenes se reducen sin perder calidad significativa |
| RF-16 | Documentación app móvil futura | Baja | Existe documentación del roadmap de app móvil |

# 03.1_Requerimientos_DevOps

| ID | Requerimiento | Prioridad | Criterios de Aceptación |
|----|--------------|----------|--------------------------|
| DEV-01 | Contenerización con Docker | Alta | El sistema se ejecuta mediante contenedores sin errores |
| DEV-02 | Ambiente de Staging | Alta | Existe entorno separado para pruebas; despliegue funcional |
| DEV-03 | Integración Continua (CI/CD) | Alta | Se ejecutan pipelines automáticos en cada cambio de código |
| DEV-04 | Pruebas de seguridad (Pentesting) | Media | Se realizan pruebas; se identifican y corrigen vulnerabilidades |
