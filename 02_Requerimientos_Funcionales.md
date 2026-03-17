## 02_Requerimientos Funcionales (RF)

# 📌 03 - Requerimientos Funcionales

| ID | Requerimiento | Prioridad | Criterios de Aceptación |
|----|--------------|----------|--------------------------|
| RF-01 | Autenticación segura con OAuth2/JWT y bloqueo tras intentos fallidos | Alta | El usuario puede iniciar sesión correctamente; el sistema genera un token válido; se bloquea la cuenta tras 3 intentos fallidos |
| RF-02 | Gestión de roles y permisos | Alta | El administrador puede asignar roles; los usuarios acceden solo a funcionalidades autorizadas |
| RF-03 | Registro de bitácora (logs) | Media | El sistema registra usuario, acción, fecha y hora; el auditor puede visualizar los logs |
| RF-04 | Registro de puntos de monitoreo georreferenciados | Alta | El usuario puede registrar coordenadas; los puntos se almacenan correctamente y se visualizan en el sistema |
| RF-05 | Carga de datos técnicos ambientales | Alta | Los técnicos ingresan datos; el sistema valida y guarda correctamente la información |
| RF-06 | Migración de datos históricos (5 años) | Media | Los datos históricos se cargan correctamente; el sistema permite su consulta sin errores |
| RF-07 | Generación de reportes estadísticos | Alta | El usuario genera reportes filtrados; la información es correcta y consistente |
| RF-08 | Consulta pública de información ambiental | Alta | El ciudadano accede sin autenticación; la información se muestra correctamente |
| RF-09 | Integración con sistema SIGIR | Media | Los datos se sincronizan correctamente con el sistema externo |
| RF-10 | Mapas dinámicos con filtros ambientales | Alta | El usuario puede filtrar por contaminante y periodo; el mapa se actualiza correctamente |
| RF-11 | Exportación de reportes (PDF/Excel) | Alta | El usuario exporta reportes sin errores en formato PDF o Excel |
| RF-12 | Solicitudes digitales de inspección | Media | El ciudadano registra solicitudes; el sistema almacena la información correctamente |
| RF-13 | Notificaciones por correo electrónico | Media | El sistema envía notificaciones correctamente ante eventos |
| RF-14 | Dashboard con indicadores ambientales | Alta | El sistema muestra indicadores actualizados y visuales claros |
| RF-15 | Compresión automática de fotografías | Baja | Las imágenes se comprimen sin afectar significativamente la calidad |
| RF-16 | Documentación de aplicación móvil futura | Baja | Existe documentación del roadmap de la app móvil |
