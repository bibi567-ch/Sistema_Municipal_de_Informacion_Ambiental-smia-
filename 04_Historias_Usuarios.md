# 04_Historias_Usuarios
## Sistema Municipal de Información Ambiental (SMIA)

**Equipo:** Anel Quiroz · Génesis Apaza · Esmeralda Alegre · Daynor Mamani · Eva Chino
**Versión:** 2.0 | **Fecha:** 17/03/2026
**Estándar:** INVEST | **Formato:** Como / Quiero / Para + Dado / Cuando / Entonces

---

## Autenticación y Seguridad

### HU-01.1

**Como** usuario del sistema
**Quiero** iniciar sesión con credenciales seguras protegidas por token JWT
**Para** acceder de forma protegida a la información ambiental del GAMLP y garantizar que solo personal autorizado opere con datos ambientales oficiales

**Criterios de Aceptación:**
- Dado que el usuario ingresa credenciales correctas, cuando inicia sesión, entonces accede al sistema con token JWT generado en < 500 ms y es redirigido al panel principal.
- Dado credenciales incorrectas, cuando intenta ingresar 3 veces consecutivas, entonces la cuenta se bloquea automáticamente por 15 minutos y se muestra el tiempo de desbloqueo.
- Dado un inicio de sesión exitoso, cuando accede, entonces se genera un token JWT con expiración de 8 horas que autentica todas las peticiones posteriores.

**Valor de negocio:** Protege la información ambiental oficial del GAMLP ante accesos no autorizados, cumpliendo la Ley N° 164 TIC y la Normativa 337.
**RF asociado:** RF-01 | **Estimación:** 3 puntos | **Prioridad:** Must Have

link mockup : https://www.figma.com/make/tKBYxgLWHbF4HgmaEIKjuD/Secure-Login-with-JWT?t=kML16D12bqdJgUJx-20&fullscreen=1&preview-route=%2Fdashboard
---

### HU-01.2

**Como** administrador
**Quiero** gestionar los accesos de los usuarios (crear, activar, desactivar, desbloquear cuentas)
**Para** garantizar que solo personas autorizadas ingresen al sistema y mantener el control operativo sin depender del área TIC del GAMLP

**Criterios de Aceptación:**
- Dado un administrador autenticado, cuando accede al panel de gestión, entonces puede ver la lista completa de usuarios con su estado (activo/bloqueado/inactivo) y rol asignado.
- Cuando modifica permisos de un usuario activo, entonces los cambios se guardan y se aplican en < 2 segundos sin cerrar la sesión del usuario afectado.
- Dado que desactiva una cuenta, cuando el usuario intenta ingresar, entonces recibe el mensaje "Cuenta inactiva. Contacte al administrador." y no puede acceder.

**Valor de negocio:** Permite al administrador gestionar el ciclo de vida de cuentas de forma autónoma, reduciendo tiempos de respuesta ante incidentes de seguridad y cumpliendo la segregación de funciones de la Normativa 337 GAMLP.
**RF asociado:** RF-01, RF-02 | **Estimación:** 2 puntos | **Prioridad:** Must Have

---

## Roles y Permisos

### HU-02.1

**Como** administrador
**Quiero** asignar roles a los usuarios (Técnico, Administrativo, Ciudadano)
**Para** controlar qué funciones pueden utilizar y garantizar la segregación de responsabilidades exigida por la Normativa 337 GAMLP

**Criterios de Aceptación:**
- Cuando asigna un rol a un usuario, entonces el usuario obtiene los permisos asociados a ese perfil en < 2 segundos sin necesidad de cerrar sesión.
- Cuando cambia un rol, entonces los permisos se actualizan y el cambio queda registrado en bitácora con nombre del administrador, fecha, hora y descripción del cambio.
- Dado que un usuario con rol Técnico intenta acceder a módulos administrativos, cuando hace clic, entonces recibe error 403 con mensaje claro de acceso denegado.

**Valor de negocio:** Garantiza la segregación de funciones requerida por la Normativa 337 GAMLP, protegiendo los datos ambientales oficiales ante modificaciones no autorizadas.
**RF asociado:** RF-02 | **Estimación:** 2 puntos | **Prioridad:** Must Have

---

### HU-02.2

**Como** usuario técnico
**Quiero** tener acceso solo a los módulos ambientales correspondientes a mi área de trabajo
**Para** evitar modificar información administrativa de otras áreas y proteger la integridad de los datos del GAMLP

**Criterios de Aceptación:**
- Dado un usuario técnico, cuando inicia sesión, entonces solo ve en el menú los módulos: Monitoreo de su área, Reportes y Consulta, sin opciones administrativas visibles.
- Si intenta acceder a otro módulo directamente por URL, entonces se le deniega el acceso con error 403 y es redirigido al panel principal.
- Dado que el administrador cambia su rol a Administrativo, cuando el usuario refresca la sesión, entonces el menú se actualiza con los módulos del nuevo rol.

**Valor de negocio:** Previene errores humanos en datos críticos para el MMAyA y asegura que cada área sea responsable exclusivamente de su información ambiental.
**RF asociado:** RF-02 | **Estimación:** 2 puntos | **Prioridad:** Must Have

---

## Auditoría

### HU-03.1

**Como** auditor de la SMGA
**Quiero** visualizar el registro inalterable de acciones del sistema
**Para** garantizar transparencia en la gestión de información y cumplir con las exigencias de auditoría de ASDI y Helvetas

**Criterios de Aceptación:**
- Cuando se realiza una acción en cualquier módulo, entonces se registra automáticamente: usuario, rol, acción ejecutada, módulo afectado, fecha, hora UTC e IP de origen, en < 100 ms.
- Cuando el auditor consulta los registros, entonces visualiza todos los logs del rango de fechas seleccionado sin omisiones, ordenados cronológicamente.
- Dado que se intenta modificar un log directamente en la base de datos, cuando el sistema verifica la integridad, entonces detecta la alteración y genera una alerta al administrador.
- Dado que necesita exportar evidencia, cuando descarga los logs, entonces obtiene un archivo CSV completo con todos los registros del período solicitado.

**Valor de negocio:** Permite demostrar transparencia ante ASDI, Helvetas y el MMAyA; condición indispensable para la continuidad del financiamiento del Proyecto Basura 0. Retención mínima de 5 años según Normativa 337.
**RF asociado:** RF-03 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

## Monitoreo Ambiental

### HU-04.1

**Como** técnico de calidad del aire de la Red MoniCA
**Quiero** registrar puntos de monitoreo con coordenadas GPS y tipo de estación
**Para** analizar la contaminación del aire con un inventario georreferenciado oficial que reemplace las hojas Excel actuales

**Criterios de Aceptación:**
- Cuando registra coordenadas, nombre y tipo de estación (pasiva/automática/activa), entonces se guardan correctamente y el punto aparece en el mapa con ícono diferenciado en < 1 segundo.
- Cuando consulta el mapa, entonces visualiza el punto con popup que muestra nombre, tipo y último dato registrado con fecha.
- Dado que ingresa coordenadas fuera del territorio municipal, cuando intenta guardar, entonces el sistema muestra una advertencia y solicita confirmación antes de continuar.

**Valor de negocio:** Centraliza el inventario de la Red MoniCA, facilitando la coordinación entre los 7 técnicos de monitoreo y cumpliendo el registro exigido por la REGAM OM 152/2010.
**RF asociado:** RF-04 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### HU-04.2

**Como** técnico de calidad del agua
**Quiero** registrar puntos de monitoreo en ríos o lagunas con coordenadas y tipo de cuerpo hídrico
**Para** evaluar la calidad hídrica con un mapa oficial de sitios de muestreo que facilite la planificación de campañas en campo

**Criterios de Aceptación:**
- Cuando registra datos (nombre, coordenadas, tipo de cuerpo hídrico), entonces se almacenan correctamente y el punto aparece en el mapa con ícono azul diferenciado de los demás tipos.
- Dado que hace clic en un punto de agua, cuando se abre el popup, entonces muestra la última medición de pH, DQO, DBO y coliformes con estado (dentro/fuera de Ley N° 1333).
- Dado que filtra por cuenca, cuando aplica el filtro, entonces el mapa muestra únicamente los puntos de esa cuenca en < 2 segundos.

**Valor de negocio:** Permite planificar y documentar el monitoreo hídrico requerido por la Ley N° 755 y el REGAM, eliminando el registro manual en hojas de campo.
**RF asociado:** RF-04 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### HU-04.3

**Como** técnico de residuos
**Quiero** registrar puntos de control en rellenos sanitarios, rutas de recolección y puntos verdes
**Para** monitorear la gestión de residuos con una visión geoespacial integrada con el sistema nacional SIGIR

**Criterios de Aceptación:**
- Cuando registra un punto (ubicación, tipo, capacidad), entonces queda guardado en el sistema y aparece en el mapa con ícono verde en < 1 segundo.
- Dado que registra una ruta de recolección, cuando traza el recorrido, entonces la ruta aparece como línea con color según estado (activa/suspendida).
- Dado que el sistema sincroniza con SIGIR, cuando confirma la sincronización, entonces los datos de pesaje del día se envían correctamente sin duplicados y se registra el estado (sincronizado/error).

**Valor de negocio:** Integra la gestión espacial de residuos con SIGIR (obligatorio por Ley N° 755), reemplazando el seguimiento en papel del Proyecto Basura 0.
**RF asociado:** RF-04, RF-05 | **Estimación:** 5 puntos | **Prioridad:** Must Have

---

### HU-04.4

**Como** técnico de ruido
**Quiero** registrar mediciones acústicas georreferenciadas con nivel de decibeles y tipo de zona
**Para** monitorear la contaminación sonora y generar evidencia técnica para el control de actividades económicas del municipio

**Criterios de Aceptación:**
- Cuando registra datos (coordenadas, nivel en dB, tipo de zona: residencial/comercial/industrial), entonces se guardan correctamente y el punto aparece en el mapa con color según umbral (verde/amarillo/rojo).
- Dado que el nivel medido supera el límite reglamentario de la zona, cuando guarda el registro, entonces el sistema genera una alerta visible en el panel del técnico responsable.
- Dado que consulta el historial de un punto, cuando accede al popup, entonces ve la evolución de niveles de dB en los últimos 6 meses en un gráfico de línea.

**Valor de negocio:** Permite documentar y actuar sobre la contaminación sonora, cumpliendo el control de actividades económicas del REGAM OM 152/2010.
**RF asociado:** RF-04 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### HU-04.5

**Como** técnico vehicular
**Quiero** registrar puntos móviles de medición con datos de gases y cantidad de vehículos inspeccionados
**Para** controlar las emisiones del parque automotor y documentar operativos para reportes al PTDI 2021-2025

**Criterios de Aceptación:**
- Cuando registra medición (ubicación, fecha, cantidad de vehículos, niveles de CO/HC/NOx), entonces se almacena correctamente y aparece en el mapa diferenciado de otros tipos de monitoreo.
- Dado que un vehículo supera los límites de emisión, cuando registra el dato, entonces el sistema lo marca con estado "Fuera de norma" y lo incluye automáticamente en el reporte del día.
- Dado que consulta el mapa de operativos filtrando por mes, cuando aplica el filtro, entonces ve solo los puntos del período seleccionado con su conteo de vehículos inspeccionados.

**Valor de negocio:** Digitaliza los operativos vehiculares, generando evidencia técnica para acciones correctivas y contribuyendo al indicador de calidad del aire del PTDI 2021-2025 Eje 4.
**RF asociado:** RF-04 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### HU-04.6

**Como** analista ambiental de la SMGA
**Quiero** visualizar todos los puntos de monitoreo (aire, agua, residuos, ruido, vehicular) en un mapa interactivo unificado
**Para** analizar la distribución geográfica de la contaminación y detectar correlaciones sin necesidad de herramientas externas como QGIS o Excel

**Criterios de Aceptación:**
- Cuando accede al mapa general, entonces visualiza todos los puntos activos categorizados por tipo con íconos y colores distintos, cargando en < 3 segundos con hasta 500 puntos simultáneos.
- Cuando filtra por tipo de monitoreo, entonces el mapa se actualiza mostrando únicamente los puntos del tipo seleccionado en < 1 segundo.
- Dado que hace zoom sobre una zona con múltiples puntos, cuando el mapa ajusta la escala, entonces los puntos cercanos se agrupan en clústeres que muestran el conteo total de estaciones en esa área.

**Valor de negocio:** Provee a la dirección de la SMGA una visión territorial integrada del estado ambiental del municipio, habilitando la toma de decisiones basada en datos geoespaciales.
**RF asociado:** RF-04, RF-10 | **Estimación:** 5 puntos | **Prioridad:** Must Have

---

## Datos Ambientales

### HU-05.1

**Como** técnico de calidad del aire
**Quiero** cargar datos de contaminantes de la Red MoniCA al sistema
**Para** calcular el ICA automáticamente con 4 decimales y eliminar el proceso manual en Excel que genera errores y demoras de hasta 2 días en la emisión de alertas

**Criterios de Aceptación:**
- Cuando ingresa datos o sube un archivo CSV de la Red MoniCA, entonces el sistema los valida, guarda y calcula el ICA con **4 decimales** según metodología EPA para el 100% de las filas válidas en < 1 segundo por registro.
- Dado que un valor de ICA supera 100, cuando se guarda el registro, entonces el sistema genera automáticamente una alerta visible en el panel en < 1 segundo.
- Dado que una fila tiene formato incorrecto, cuando el proceso la detecta, entonces la omite, registra el error con número de fila y tipo de problema, y continúa procesando las demás.

**Valor de negocio:** Reduce el tiempo de emisión de alertas de contaminación del aire en un 60%, cumpliendo el KPI de respuesta definido por ASDI para el Proyecto Basura 0.
**RF asociado:** RF-05 | **Estimación:** 5 puntos | **Prioridad:** Must Have

---

### HU-05.2

**Como** técnico de calidad del agua
**Quiero** ingresar parámetros físico-químicos como DBO, DQO, pH, coliformes y turbidez al sistema
**Para** evaluar la calidad hídrica comparando automáticamente contra los límites de la Ley N° 1333 y generar alertas cuando haya incumplimientos

**Criterios de Aceptación:**
- Cuando ingresa datos de análisis de laboratorio, entonces se almacenan correctamente vinculados al punto de muestreo y a la fecha de toma de muestra.
- Dado que un parámetro supera el límite de la Ley N° 1333, cuando se guarda el registro, entonces aparece marcado en rojo con el valor medido y el límite permisible correspondiente en < 1 segundo.
- Dado que consulta el historial de un punto de muestreo, cuando accede a sus registros, entonces ve tabla con todos los análisis ordenados por fecha y estado de cumplimiento de cada uno.

**Valor de negocio:** Automatiza la verificación de cumplimiento de la Ley N° 1333, reduciendo el tiempo de detección de incumplimientos hídricos de días a segundos.
**RF asociado:** RF-05 | **Estimación:** 5 puntos | **Prioridad:** Must Have

---

### HU-05.3

**Como** técnico de residuos
**Quiero** registrar el pesaje diario de residuos en el relleno sanitario Sak'a Churu
**Para** controlar los volúmenes ingresados y sincronizarlos automáticamente con SIGIR, cumpliendo el reporte obligatorio al MMAyA bajo la Ley N° 755

**Criterios de Aceptación:**
- Cuando registra datos de pesaje (tipo de residuo, peso en toneladas, operador, fecha), entonces se guardan correctamente y se envían automáticamente a SIGIR.
- Dado que SIGIR no responde al momento de sincronizar, cuando se detecta el error, entonces el sistema guarda el registro localmente, reintenta cada 30 minutos y notifica al técnico con el estado de sincronización.
- Dado que consulta el consolidado mensual, cuando genera el reporte, entonces ve el total de toneladas por tipo de residuo con estado SIGIR (sincronizado/pendiente/error) para cada registro.

**Valor de negocio:** Asegura el reporte obligatorio de residuos al MMAyA (Ley N° 755) eliminando la doble carga manual de datos en el sistema municipal y en el sistema nacional.
**RF asociado:** RF-05 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### HU-05.4

**Como** técnico de ruido
**Quiero** registrar los niveles de decibeles medidos en campo durante operativos de control acústico
**Para** monitorear la contaminación sonora y construir un historial oficial que respalde las acciones de control ambiental del GAMLP

**Criterios de Aceptación:**
- Cuando registra una medición (punto, nivel en dB, hora, tipo de zona), entonces se almacena correctamente vinculada al punto georreferenciado correspondiente.
- Dado que el nivel supera el límite de la zona (ej. > 65 dB en zona residencial nocturna), cuando se guarda, entonces el sistema lo clasifica como "Excedencia" y lo incluye en el reporte diario automáticamente.
- Dado que genera el reporte mensual de ruido con filtro por zona, cuando lo descarga, entonces obtiene tabla de mediciones con porcentaje de excedencias y promedio de dB por punto.

**Valor de negocio:** Habilita el control documentado de la contaminación acústica en el municipio, cumpliendo el componente de control de actividades del REGAM OM 152/2010.
**RF asociado:** RF-05 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### HU-05.5

**Como** técnico vehicular
**Quiero** registrar las mediciones de gases (CO, HC, NOx, opacidad) realizadas en operativos al parque automotor
**Para** evaluar el estado de cumplimiento ambiental de los vehículos controlados y generar estadísticas de contaminación vehicular para el PTDI 2021-2025

**Criterios de Aceptación:**
- Cuando registra datos (placa, tipo de vehículo, año, valores CO/HC/NOx), entonces se guardan correctamente con indicación automática de si está dentro o fuera de norma según límites vigentes.
- Dado que un vehículo está fuera de norma, cuando se guarda el registro, entonces queda marcado como "No apto" con registro de infracción vinculado a la placa.
- Dado que genera el reporte del operativo y lo descarga, cuando lo abre, entonces incluye: total inspeccionados, % de cumplimiento y listado de vehículos no aptos con placa, niveles medidos y fecha.

**Valor de negocio:** Digitaliza los operativos vehiculares generando evidencia técnica para acciones correctivas y contribuyendo al indicador de calidad del aire del PTDI 2021-2025 Eje 4.
**RF asociado:** RF-05 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### HU-05.6

**Como** analista ambiental
**Quiero** que el sistema calcule automáticamente todos los indicadores ambientales (ICA, índices hídricos, porcentaje de excedencias) al ingresar datos
**Para** evitar errores de cálculo manual en Excel y asegurar que todos los reportes usen la misma metodología oficial sin discrepancias entre áreas

**Criterios de Aceptación:**
- Cuando se ingresan datos de cualquier módulo, entonces el sistema calcula el indicador correspondiente automáticamente sin intervención manual del técnico.
- Dado que el administrador actualiza los parámetros de una metodología de cálculo, cuando se confirma el cambio, entonces todos los cálculos futuros usan la nueva fórmula sin modificar los registros históricos.
- Dado que se compara el resultado del sistema con el cálculo manual usando los mismos datos de entrada, cuando se ejecuta la prueba, entonces los resultados coinciden en el 100% de los casos.

**Valor de negocio:** Garantiza consistencia metodológica en todos los reportes del GAMLP, eliminando las discrepancias entre áreas que actualmente generan correcciones en los informes al MMAyA.
**RF asociado:** RF-05 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

## Históricos

### HU-06.1

**Como** planificador de la SMGA
**Quiero** consultar datos históricos de monitoreo ambiental de al menos 5 años anteriores
**Para** analizar tendencias ambientales a largo plazo y generar los informes de evolución que exigen ASDI y Helvetas para evaluar el impacto del Proyecto Basura 0

**Criterios de Aceptación:**
- Cuando consulta datos aplicando filtro por año y área ambiental, entonces se muestran correctamente todos los registros del período seleccionado en < 5 segundos.
- Dado que aplica filtro de rango de años, cuando genera la visualización, entonces puede ver tendencias desde el año más antiguo disponible hasta la fecha actual en un gráfico de línea.
- Dado que la migración histórica está completa, cuando ejecuta cualquier consulta, entonces los datos históricos son accesibles con la misma interfaz que los datos actuales, sin distinción de origen.

**Valor de negocio:** Centraliza 5 años de información dispersa en Excel y papel, habilitando el análisis de tendencias exigido por los financiadores ASDI y Helvetas para evaluar el impacto real del Proyecto Basura 0.
**RF asociado:** RF-06 | **Estimación:** 5 puntos | **Prioridad:** Must Have

---

## Reportes

### HU-07.1

**Como** jefe del área de calidad del aire de la SMGA
**Quiero** generar reportes filtrados de monitoreo atmosférico por fecha, estación y contaminante
**Para** presentar informes oficiales al MMAyA con datos de la Red MoniCA sin procesamiento manual en Excel

**Criterios de Aceptación:**
- Cuando genera el reporte con filtros seleccionados, entonces los datos son correctos, incluyen ICA calculado y gráfica de tendencia, y se muestran en < 5 segundos.
- Cuando aplica filtros de fecha, estación y contaminante, entonces se reflejan exactamente en el reporte sin registros fuera del criterio seleccionado.
- Dado que descarga el reporte en PDF, cuando lo abre, entonces incluye logo GAMLP, nombre del área, rango de fechas y nombre del usuario que lo generó.

**Valor de negocio:** Elimina 3-5 días de trabajo manual por informe, cumpliendo los plazos de entrega de reportes oficiales al MMAyA establecidos en la Ley N° 755.
**RF asociado:** RF-07 | **Estimación:** 3 puntos | **Prioridad:** Must Have

**Link mockup:**            https://www.figma.com/make/JyabLSV7yYMC06s2rfGVih/Generar-reportes-de-calidad?t=2iQ4JZxE2z1OOko8-20&fullscreen=1
---

### HU-07.2

**Como** jefe del área de calidad del agua de la SMGA
**Quiero** generar reportes de calidad hídrica filtrados por cuenca, punto de muestreo y parámetro
**Para** documentar el estado de cumplimiento de la Ley N° 1333 en los cuerpos de agua del municipio y presentarlos al MMAyA

**Criterios de Aceptación:**
- Cuando genera el reporte con filtros de cuenca y rango de fechas, entonces los datos son correctos e incluyen tabla con valores, límite Ley 1333 y estado de cumplimiento (Cumple/No cumple) en < 5 segundos.
- Cuando aplica filtros, entonces se reflejan en el reporte mostrando únicamente los registros del período y cuenca seleccionados.
- Dado que hay excedencias en el período, cuando descarga el PDF, entonces incluye sección de resumen con porcentaje de excedencias por parámetro.

**Valor de negocio:** Automatiza la generación de informes hídricos oficiales para el MMAyA, reduciendo el riesgo de inconsistencias en los datos reportados bajo la Ley N° 1333.
**RF asociado:** RF-07 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### HU-07.3

**Como** jefe del área de residuos de la SMGA
**Quiero** generar reportes del relleno sanitario Sak'a Churu con datos de pesaje y estado de sincronización SIGIR
**Para** cumplir la rendición de cuentas mensual al MMAyA y verificar que los datos estén integrados correctamente al sistema nacional

**Criterios de Aceptación:**
- Cuando genera el reporte seleccionando mes y tipo de residuo, entonces los datos son correctos con consolidado de toneladas por día y estado SIGIR de cada registro en < 5 segundos.
- Cuando aplica filtros de fecha y tipo de residuo, entonces se reflejan exactamente en el reporte sin registros fuera del criterio seleccionado.
- Dado que hay registros pendientes de sincronización, cuando genera el reporte, entonces aparece alerta con número de registros afectados y botón para reintentar la sincronización.

**Valor de negocio:** Garantiza el reporte obligatorio de residuos al MMAyA (Ley N° 755) y facilita la auditoría del Proyecto Basura 0 por parte de ASDI y Swisscontact.
**RF asociado:** RF-07 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### HU-07.4

**Como** jefe del área de control de ruido de la SMGA
**Quiero** generar reportes de contaminación acústica filtrados por zona y período
**Para** analizar información sobre excedencias de ruido y fundamentar acciones de control ambiental sobre actividades económicas ruidosas

**Criterios de Aceptación:**
- Cuando genera el reporte con filtro de zona y mes, entonces los datos son correctos e incluyen tabla de excedencias por punto con nivel promedio de dB en < 5 segundos.
- Cuando aplica filtros de zona y período, entonces se reflejan en el reporte mostrando únicamente los puntos y fechas seleccionados.
- Dado que descarga el PDF, cuando lo abre, entonces incluye mapa de distribución acústica y tabla de excedencias con fecha, nivel medido y límite aplicable.

**Valor de negocio:** Provee evidencia técnica documentada para las acciones de control sobre fuentes de ruido, cumpliendo el control de actividades del REGAM OM 152/2010.
**RF asociado:** RF-07 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### HU-07.5

**Como** jefe del área de emisiones vehiculares de la SMGA
**Quiero** generar reportes de los operativos de control vehicular con estadísticas de cumplimiento
**Para** analizar información sobre contaminación vehicular y evaluar la efectividad de los operativos ante las autoridades municipales

**Criterios de Aceptación:**
- Cuando genera el reporte seleccionando mes y zona de operativo, entonces los datos son correctos e incluyen: total inspeccionados, % de cumplimiento y ranking de contaminantes frecuentes en < 5 segundos.
- Cuando aplica filtros de mes y zona, entonces se reflejan exactamente en el reporte sin vehículos fuera del período o zona seleccionados.
- Dado que descarga el Excel, cuando lo abre, entonces incluye hoja de detalle con todos los vehículos inspeccionados, placa, resultado y fecha.

**Valor de negocio:** Habilita la evaluación basada en datos de la política de control vehicular del GAMLP, contribuyendo al indicador de calidad del aire del PTDI 2021-2025 Eje 4.
**RF asociado:** RF-07 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### HU-07.6

**Como** analista ambiental de la SMGA
**Quiero** visualizar gráficos estadísticos interactivos de todos los módulos de monitoreo
**Para** analizar tendencias, estacionalidades y correlaciones ambientales sin exportar datos a herramientas externas como Excel o Power BI

**Criterios de Aceptación:**
- Cuando accede a la sección de estadísticas y selecciona módulo, parámetro y rango de fechas, entonces visualiza gráficos correctos actualizados en < 3 segundos.
- Dado que pasa el cursor sobre un punto del gráfico, cuando se despliega el tooltip, entonces ve el valor exacto, la fecha y el estado respecto a la norma aplicable.
- Dado que activa la opción de comparar dos períodos, cuando el gráfico se actualiza, entonces muestra ambas líneas con colores diferenciados y leyenda descriptiva.

**Valor de negocio:** Acelera el análisis técnico de datos ambientales reduciendo el tiempo de preparación de informes de tendencias de días a minutos para los responsables de cada área.
**RF asociado:** RF-07 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

## Consulta Pública

### HU-08.1

**Como** ciudadano del Municipio de La Paz
**Quiero** consultar información ambiental (calidad del aire, alertas, estado de ríos) sin necesidad de registrarme
**Para** informarme sobre el estado del ambiente de mi ciudad y tomar decisiones sobre mi salud y la de mi familia (ej. evitar zonas contaminadas), cumpliendo el derecho a la información de la Ley de Transparencia del GAMLP

**Criterios de Aceptación:**
- Cuando accede al portal público sin sesión iniciada, entonces visualiza el mapa de calidad del aire por zonas con colores ICA (Verde/Amarillo/Naranja/Rojo) cargando en < 4 segundos.
- Dado que hace clic en una zona del mapa, cuando se abre el popup, entonces ve el ICA actual, categoría de calidad y fecha de la última actualización.
- Dado que hay alertas ambientales activas, cuando carga la página, entonces aparecen en un banner superior con zona afectada y recomendación de acción para la ciudadanía.

**Valor de negocio:** Cumple la Ley de Transparencia del GAMLP y el objetivo de participación ciudadana del Proyecto Basura 0, apuntando al KPI de 5 000 usuarios únicos mensuales en el primer trimestre. Cumple WCAG 2.1 AA.
**RF asociado:** RF-08 | **Estimación:** 3 puntos | **Prioridad:** Must Have
**Link mockup:**     https://www.figma.com/make/q9aZzew39qF7jf3B6kuWUk/Consulta-de-informaci%C3%B3n-ambiental?t=blDQs7fJ4NUN8uid-20&fullscreen=1

---

## Integración

### HU-09.1

**Como** encargado de residuos de la SMGA
**Quiero** sincronizar los datos de pesaje y gestión de residuos con el sistema nacional SIGIR
**Para** mantener los datos actualizados en el sistema nacional y cumplir con la obligación de reporte al MMAyA establecida en la Ley N° 755

**Criterios de Aceptación:**
- Cuando sincroniza los datos del día, entonces los datos se actualizan correctamente en SIGIR sin duplicados y el sistema registra el resultado (éxito/error) con timestamp.
- Dado que SIGIR no responde durante la sincronización, cuando se detecta el error, entonces el sistema almacena los datos localmente, reintenta automáticamente cada 30 minutos y notifica al técnico.
- Dado que la sincronización se completa con éxito, cuando el encargado consulta el estado, entonces ve confirmación con número de registros enviados, fecha y hora de la última sincronización exitosa.

**Valor de negocio:** Asegura el cumplimiento de la Ley N° 755 (SIGIR) evitando sanciones al GAMLP por reporte tardío o incompleto de datos de residuos al MMAyA.
**RF asociado:** RF-05 | **Estimación:** 5 puntos | **Prioridad:** Must Have

---

## Mapas

### HU-10.1

**Como** analista ambiental de la SMGA
**Quiero** filtrar los mapas por tipo de contaminante y periodo de tiempo
**Para** analizar la distribución espacial y temporal de la contaminación, identificando zonas críticas sin necesidad de exportar datos a herramientas externas

**Criterios de Aceptación:**
- Cuando aplica filtro por contaminante y rango de fechas, entonces el mapa se actualiza mostrando únicamente los puntos que cumplen los criterios en < 2 segundos.
- Dado que combina hasta 3 filtros simultáneos (contaminante + período + nivel de alerta), cuando los aplica, entonces el sistema los procesa sin error y muestra resultados correctos.
- Dado que limpia todos los filtros activos, cuando hace clic en "Limpiar", entonces el mapa vuelve a su estado original con todos los puntos en < 1 segundo.

**Valor de negocio:** Acelera la identificación de patrones y zonas críticas de contaminación, mejorando la capacidad de respuesta de la SMGA ante eventos ambientales.
**RF asociado:** RF-10 | **Estimación:** 3 puntos | **Prioridad:** Should Have

---

## Exportación

### HU-11.1

**Como** técnico o Director de la SMGA
**Quiero** exportar reportes en formato PDF con membrete oficial o Excel con datos tabulados
**Para** compartir información ambiental oficial con el MMAyA, ASDI y Helvetas sin necesidad de reformatear manualmente los datos del sistema

**Criterios de Aceptación:**
- Cuando exporta seleccionando formato PDF, entonces se genera el archivo con logo GAMLP, nombre del usuario, fecha de generación y datos filtrados correctamente en < 10 segundos.
- Dado que selecciona formato Excel, cuando se genera el archivo, entonces obtiene un `.xlsx` con headers descriptivos en la primera fila y sin datos truncados.
- Dado que el reporte tiene más de 1 000 filas, cuando inicia la exportación, entonces el sistema muestra barra de progreso y el archivo se descarga al completarse sin error.

**Valor de negocio:** Elimina el reprocesamiento manual de datos para informes oficiales, reduciendo de 2 días a minutos la preparación de reportes para el MMAyA y los financiadores.
**RF asociado:** RF-11 | **Estimación:** 3 puntos | **Prioridad:** Should Have

---

## Ciudadano

### HU-12.1

**Como** ciudadano del Municipio de La Paz
**Quiero** registrar solicitudes de inspección ambiental desde el portal web
**Para** pedir inspecciones de problemas ambientales en mi barrio (vertido ilegal, quema de basura, ruido excesivo) sin necesidad de ir presencialmente a las oficinas de la SMGA

**Criterios de Aceptación:**
- Cuando registra la solicitud con tipo de problema, descripción y ubicación en el mapa, entonces se guarda correctamente y el sistema genera un número de seguimiento único en < 1 segundo.
- Dado que envía la solicitud, cuando se registra en el sistema, entonces aparece en tiempo real en el panel de gestión interna de los técnicos de la SMGA.
- Dado que tiene su número de seguimiento, cuando lo ingresa en el portal sin autenticarse, entonces ve el estado actual (Recibida / En revisión / En proceso / Cerrada) y la fecha de última actualización.

**Valor de negocio:** Digitaliza la atención ciudadana ambiental eliminando filas presenciales y contribuyendo al KPI de 5 000 usuarios únicos mensuales en el portal público del primer trimestre.
**RF asociado:** RF-12 | **Estimación:** 5 puntos | **Prioridad:** Should Have

---

## Notificaciones

### HU-13.1

**Como** usuario que registró una solicitud de inspección
**Quiero** recibir notificaciones automáticas por correo electrónico sobre el estado de mi solicitud
**Para** estar informado sobre el avance de mi denuncia sin necesidad de ingresar al portal cada vez, mejorando la percepción de transparencia del GAMLP

**Criterios de Aceptación:**
- Cuando ocurre un evento relevante (registro de solicitud, cambio de estado), entonces el usuario recibe notificación por correo con número de seguimiento, descripción y estado actualizado en < 2 minutos.
- Dado que el correo se envía, cuando se abre en Gmail, Outlook o webmail, entonces el formato HTML se visualiza correctamente sin elementos rotos ni imágenes faltantes.
- Dado que el técnico marca la solicitud como "Cerrada", cuando se envía la notificación, entonces incluye el resumen de las acciones tomadas y la fecha de cierre.

**Valor de negocio:** Mejora la percepción de transparencia y efectividad del GAMLP ante la ciudadanía, alineándose con el objetivo de participación ciudadana del Proyecto Basura 0.
**RF asociado:** RF-13 | **Estimación:** 2 puntos | **Prioridad:** Could Have

---

## Dashboard

### HU-14.1

**Como** Secretario/a Municipal de Gestión Ambiental
**Quiero** visualizar un panel con indicadores ambientales consolidados y actualizados en tiempo real
**Para** tomar decisiones estratégicas basadas en datos sin depender de reportes manuales de cada área técnica

**Criterios de Aceptación:**
- Cuando accede al dashboard, entonces visualiza en < 3 segundos: ICA promedio del día, alertas activas por tipo, número de inspecciones del mes y porcentaje de cumplimiento Ley 1333.
- Dado que hace clic en un indicador del panel, cuando se expande, entonces ve el detalle con gráfica de tendencia de los últimos 30 días.
- Dado que se registran nuevos datos en el sistema, cuando actualiza el dashboard, entonces los widgets reflejan los datos más recientes sin necesidad de recargar la página completa.

**Valor de negocio:** Habilita la toma de decisiones en tiempo real para la dirección de la SMGA, cumpliendo el KPI de reducción del 60% en el tiempo de emisión de alertas definido por ASDI.
**RF asociado:** RF-14 | **Estimación:** 5 puntos | **Prioridad:** Could Have

---

## Imágenes

### HU-15.1

**Como** técnico de campo de la SMGA
**Quiero** que las fotografías que subo al sistema se optimicen y compriman automáticamente
**Para** mejorar el rendimiento del sistema y poder cargar evidencia fotográfica desde campo sin preocuparme por el tamaño de los archivos ni el consumo de datos móviles

**Criterios de Aceptación:**
- Cuando sube una imagen en JPG o PNG, entonces se comprime automáticamente a formato WebP con calidad 80%, reduciendo el tamaño en al menos **40%** sin intervención del usuario.
- Dado que la imagen se comprime, cuando la visualiza en el sistema, entonces la resolución mínima conservada es **1024 × 768 px** y los detalles relevantes para la inspección son visibles.
- Dado que la compresión falla por algún error técnico, cuando ocurre, entonces el sistema guarda la imagen original y notifica al técnico que la optimización no pudo realizarse.

**Valor de negocio:** Reduce el espacio de almacenamiento de evidencia fotográfica en al menos 40%, optimizando los costos de infraestructura del Data Center del GAMLP.
**RF asociado:** RF-15 | **Estimación:** 2 puntos | **Prioridad:** Could Have

---

## Roadmap

### HU-16.1

**Como** gestor del proyecto SMIA
**Quiero** documentar los requerimientos de la aplicación móvil nativa en el repositorio
**Para** planificación de fases futuras, de modo que el equipo de la siguiente fase tenga una base técnica clara sin repetir el levantamiento de requerimientos desde cero

**Criterios de Aceptación:**
- Dado que la fase 1 se cierra, cuando se entrega la documentación final, entonces el repositorio incluye un archivo `ROADMAP_MOVIL.md` con: funcionalidades previstas, plataformas objetivo (iOS/Android), tecnología sugerida y dependencias de la fase 1.
- Dado que existe el documento del roadmap, cuando un nuevo equipo lo lee, entonces entiende el alcance, las restricciones y los requerimientos pendientes sin necesidad de consultar al equipo original.
- Dado que se entrega al GAMLP, cuando el equipo TIC lo revisa, entonces el documento cumple los estándares de transferencia tecnológica de la Normativa 337.

**Valor de negocio:** Protege la inversión de conocimiento del equipo actual y reduce el tiempo de inicio de la fase 2, cumpliendo la transferencia tecnológica requerida por la Normativa 337 GAMLP.
**RF asociado:** RF-16 | **Estimación:** 1 punto | **Prioridad:** Won't Have — Fase 2

---

## Requerimientos No Funcionales

### RNF-01 — Seguridad (Hashing de contraseñas)

**Como** encargado de seguridad del sistema SMIA
**Quiero** proteger las contraseñas de todos los usuarios mediante algoritmos de hashing irreversible (bcrypt o Argon2id)
**Para** evitar accesos no autorizados ante posibles vulneraciones de la base de datos y cumplir con ISO/IEC 27001 Control A.9.4.3

**Criterios de Aceptación:**
- Dado que un usuario se registra o cambia su contraseña, cuando guarda su contraseña, entonces se almacena en formato hash (bcrypt factor 12 o Argon2id 64MB) y nunca en texto plano.
- Dado un intento de acceso a la base de datos, cuando se visualizan las contraseñas en la tabla de usuarios, entonces no son legibles: el resultado es un hash irreconocible.
- Dado un inicio de sesión, cuando el usuario ingresa su contraseña, entonces el sistema valida mediante comparación de hashes en < 500 ms sin exponer el hash en ninguna respuesta HTTP.

**Valor de negocio:** Protege la información sensible del personal del GAMLP ante ataques de fuerza bruta o filtraciones de BD, cumpliendo ISO/IEC 27001 y la Ley N° 164 TIC.
**RNF asociado:** RNF-01 | **Estimación:** 2 puntos | **Prioridad:** Must Have

---

### RNF-02 — Rendimiento

**Como** usuario del sistema (técnico, administrativo o ciudadano)
**Quiero** que las consultas y búsquedas respondan en tiempos rápidos
**Para** mejorar la experiencia de uso y que el sistema sea adoptado como herramienta de trabajo diario reemplazando Excel

**Criterios de Aceptación:**
- Dado que el sistema tiene hasta 10 000 registros, cuando se realiza una consulta o búsqueda, entonces responde en **menos de 1 segundo** con los resultados correctos.
- Dado múltiples usuarios concurrentes (hasta 20 simultáneos), cuando acceden al sistema al mismo tiempo, entonces el rendimiento se mantiene estable con tiempo de respuesta P95 **< 2 segundos** y tasa de error **< 1%**.
- Dado que se ejecuta prueba de carga con Locust (20 usuarios, 5 minutos), cuando se revisan los resultados, entonces el P95 de tiempo de respuesta es < 2 segundos en operaciones estándar.

**Valor de negocio:** Garantiza que los 7 técnicos de la SMGA adopten el sistema como herramienta diaria, superando la experiencia de uso de Excel sin tiempos de espera que frustren la adopción.
**RNF asociado:** RNF-02 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### RNF-03 — Compatibilidad (Responsive)

**Como** usuario móvil (técnico en campo o ciudadano)
**Quiero** usar el sistema desde cualquier dispositivo (celular, tableta o computadora) sin instalar aplicaciones
**Para** acceder al sistema y registrar datos desde el campo con el dispositivo disponible, sin limitaciones de plataforma

**Criterios de Aceptación:**
- Dado que el usuario accede desde un celular Android con pantalla de 360 px, cuando navega por el sistema, entonces la interfaz se adapta correctamente sin elementos solapados ni texto truncado.
- Dado diferentes tamaños de pantalla (360 px a 1920 px), cuando el usuario visualiza el sistema en Chrome, Firefox o Edge, entonces no hay errores de diseño ni funcionalidades inaccesibles.
- Dado que se ejecuta prueba de usabilidad SUS con 5 usuarios de la SMGA, cuando se tabulan los resultados, entonces la puntuación promedio es **≥ 70 / 100**.

**Valor de negocio:** Permite a los técnicos registrar datos directamente en campo desde el celular, eliminando la doble carga (papel en campo + Excel en oficina) que genera errores y pérdida de información.
**RNF asociado:** RNF-03 | **Estimación:** 3 puntos | **Prioridad:** Should Have

---

## Requerimientos DevOps

### DEV-01 — Contenerización con Docker

**Como** ingeniero DevOps del equipo de desarrollo
**Quiero** ejecutar el sistema completo en contenedores Docker Compose
**Para** facilitar el despliegue y portabilidad, garantizando que el entorno de desarrollo, staging y producción sean idénticos y el equipo TIC del GAMLP pueda operar el sistema de forma autónoma

**Criterios de Aceptación:**
- Dado el código del sistema en el repositorio, cuando el equipo TIC ejecuta `docker compose up` en un servidor nuevo, entonces la aplicación completa (frontend + backend + BD) inicia correctamente en < 5 minutos.
- Dado un entorno nuevo sin configuraciones previas, cuando se despliega el contenedor siguiendo el README, entonces funciona sin configuraciones adicionales más allá del archivo `.env`.
- Dado que se revisa el repositorio, cuando se inspeccionan los archivos raíz, entonces existen `Dockerfile`, `docker-compose.yml` y `.env.example` con documentación de uso.

**Valor de negocio:** Elimina el problema "funciona en mi máquina" y garantiza que el equipo TIC del GAMLP opere el sistema autónomamente, cumpliendo la transferencia tecnológica de la Normativa 337.
**RNF asociado:** RNF-06 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### DEV-02 — Ambiente de Staging

**Como** equipo de desarrollo del SMIA
**Quiero** probar el sistema en un entorno de staging idéntico a producción
**Para** validar cada módulo antes de publicarlo en producción, protegiendo los datos reales del GAMLP ante errores no detectados

**Criterios de Aceptación:**
- Dado un cambio nuevo en el sistema, cuando se despliega en staging, entonces se refleja en el entorno de staging con la misma configuración de Docker, BD y variables de entorno que producción.
- Dado pruebas realizadas en staging por técnicos de la SMGA, cuando detectan errores, entonces estos no afectan producción y quedan documentados en el issue tracker del repositorio.
- Dado que el técnico aprueba el módulo en staging, cuando se da la aprobación formal, entonces el equipo puede proceder al despliegue en producción sin requerir correcciones posteriores.

**Valor de negocio:** Reduce el riesgo de errores en producción, protegiendo la integridad de los datos ambientales oficiales del GAMLP ante lanzamientos con defectos no detectados.
**RNF asociado:** RNF-06 | **Estimación:** 2 puntos | **Prioridad:** Must Have

---

### DEV-03 — Integración Continua (CI/CD)

**Como** desarrollador del equipo SMIA
**Quiero** usar pipelines CI/CD con GitHub Actions para automatizar pruebas y verificaciones en cada Pull Request
**Para** automatizar la detección de errores antes de fusionar código y garantizar que la rama `main` siempre esté en estado desplegable

**Criterios de Aceptación:**
- Dado un commit en el repositorio y un Pull Request abierto, cuando se realiza el push, entonces se ejecuta automáticamente el pipeline: linting + pruebas unitarias + verificación de cobertura ≥ 70%.
- Dado fallos en el código o pruebas, cuando se ejecuta el pipeline, entonces se notifica el error con detalle del fallo y el PR queda bloqueado para fusión hasta que se corrija.
- Dado que todas las verificaciones pasan, cuando el pipeline termina en < 5 minutos, entonces el PR queda habilitado para revisión y fusión por un segundo integrante del equipo.

**Valor de negocio:** Garantiza la calidad continua del código reduciendo bugs en producción y cumpliendo el requisito de CI del TDR GAMLP con métricas DORA medibles.
**RNF asociado:** RNF-07 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

### DEV-04 — Pruebas de Seguridad (Pentesting)

**Como** equipo de seguridad del proyecto SMIA
**Quiero** realizar pruebas de penetración con OWASP ZAP sobre todos los endpoints del sistema
**Para** detectar y corregir vulnerabilidades críticas antes de que el sistema esté expuesto a usuarios reales, protegiendo los datos ambientales oficiales y la información ciudadana

**Criterios de Aceptación:**
- Dado el sistema desplegado en staging, cuando se ejecutan las pruebas de seguridad con OWASP ZAP, entonces se identifican vulnerabilidades clasificadas por severidad (Crítica/Alta/Media/Baja) en un reporte formal.
- Dado vulnerabilidades Críticas o Altas detectadas, cuando se corrigen y se vuelve a ejecutar el escaneo, entonces el sistema mejora su seguridad hasta no tener ninguna vulnerabilidad Crítica o Alta sin resolver.
- Dado que el sistema pasa el pentesting, cuando se entrega la documentación al GAMLP, entonces el reporte final (sin vulnerabilidades Críticas ni Altas) se incluye en el paquete de transferencia tecnológica de la Normativa 337.

**Valor de negocio:** Protege los datos ambientales y la información ciudadana ante ataques externos, cumpliendo el requisito de seguridad proactiva del TDR y la Ley N° 164 TIC.
**RNF asociado:** RNF-08 | **Estimación:** 3 puntos | **Prioridad:** Must Have

---

## Resumen del Product Backlog

| ID | Historia | Puntos | Prioridad | RF/RNF |
|----|----------|--------|-----------|--------|
| HU-01.1 | Acceso seguro al sistema | 3 | Must Have | RF-01 |
| HU-01.2 | Gestión de accesos por administrador | 2 | Must Have | RF-01, RF-02 |
| HU-02.1 | Asignación de roles y permisos | 2 | Must Have | RF-02 |
| HU-02.2 | Restricción de acceso por módulo | 2 | Must Have | RF-02 |
| HU-03.1 | Auditoría inalterable de acciones | 3 | Must Have | RF-03 |
| HU-04.1 | Puntos de monitoreo de aire | 3 | Must Have | RF-04 |
| HU-04.2 | Puntos de monitoreo de agua | 3 | Must Have | RF-04 |
| HU-04.3 | Puntos de control de residuos | 5 | Must Have | RF-04, RF-05 |
| HU-04.4 | Mediciones acústicas georreferenciadas | 3 | Must Have | RF-04 |
| HU-04.5 | Puntos móviles vehiculares | 3 | Must Have | RF-04 |
| HU-04.6 | Mapa unificado interactivo | 5 | Must Have | RF-04, RF-10 |
| HU-05.1 | Carga de datos de aire — ICA | 5 | Must Have | RF-05 |
| HU-05.2 | Parámetros de calidad del agua | 5 | Must Have | RF-05 |
| HU-05.3 | Pesaje de residuos + SIGIR | 3 | Must Have | RF-05 |
| HU-05.4 | Niveles de ruido (dB) | 3 | Must Have | RF-05 |
| HU-05.5 | Mediciones de gases vehiculares | 3 | Must Have | RF-05 |
| HU-05.6 | Cálculo automático de indicadores | 3 | Must Have | RF-05 |
| HU-06.1 | Consulta de datos históricos | 5 | Must Have | RF-06 |
| HU-07.1 | Reporte de calidad del aire | 3 | Must Have | RF-07 |
| HU-07.2 | Reporte de calidad hídrica | 3 | Must Have | RF-07 |
| HU-07.3 | Reporte de gestión de residuos | 3 | Must Have | RF-07 |
| HU-07.4 | Reporte de contaminación acústica | 3 | Must Have | RF-07 |
| HU-07.5 | Reporte de emisiones vehiculares | 3 | Must Have | RF-07 |
| HU-07.6 | Gráficos estadísticos interactivos | 3 | Must Have | RF-07 |
| HU-08.1 | Consulta pública sin registro | 3 | Must Have | RF-08 |
| HU-09.1 | Sincronización con SIGIR | 5 | Must Have | RF-05 |
| HU-10.1 | Filtros avanzados en mapa | 3 | Should Have | RF-10 |
| HU-11.1 | Exportación PDF / Excel | 3 | Should Have | RF-11 |
| HU-12.1 | Solicitud ciudadana de inspección | 5 | Should Have | RF-12 |
| HU-13.1 | Notificaciones por correo | 2 | Could Have | RF-13 |
| HU-14.1 | Dashboard gerencial | 5 | Could Have | RF-14 |
| HU-15.1 | Optimización de fotografías | 2 | Could Have | RF-15 |
| HU-16.1 | Documentación app móvil | 1 | Won't Have | RF-16 |
| RNF-01 | Hashing de contraseñas | 2 | Must Have | RNF-01 |
| RNF-02 | Rendimiento < 1s | 3 | Must Have | RNF-02 |
| RNF-03 | Responsive + SUS ≥ 70 | 3 | Should Have | RNF-03 |
| DEV-01 | Docker Compose | 3 | Must Have | RNF-06 |
| DEV-02 | Ambiente de staging | 2 | Must Have | RNF-06 |
| DEV-03 | Pipeline CI/CD | 3 | Must Have | RNF-07 |
| DEV-04 | Pentesting OWASP | 3 | Must Have | RNF-08 |
| **TOTAL** | | **122 puntos** | | |
