# 04_Historias_Usuarios

## Autenticación y Seguridad

### HU-01.1
**Como** usuario del sistema  
**Quiero** iniciar sesión con credenciales seguras  
**Para** acceder de forma protegida a la información ambiental  

**Criterios de Aceptación:**
- Dado que el usuario ingresa credenciales correctas, cuando inicia sesión, entonces accede al sistema.
- Dado credenciales incorrectas, cuando intenta ingresar 3 veces, entonces la cuenta se bloquea.
- Dado un inicio de sesión exitoso, cuando accede, entonces se genera un token de autenticación.

---

### HU-01.2
**Como** administrador  
**Quiero** gestionar los accesos de los usuarios  
**Para** garantizar que solo personas autorizadas ingresen al sistema  

**Criterios de Aceptación:**
- Dado un administrador autenticado, cuando accede al panel, entonces puede ver usuarios.
- Cuando modifica permisos, entonces los cambios se guardan correctamente.

---

## Roles y Permisos

### HU-02.1
**Como** administrador  
**Quiero** asignar roles a los usuarios  
**Para** controlar qué funciones pueden utilizar  

**Criterios de Aceptación:**
- Cuando asigna un rol, entonces el usuario obtiene permisos asociados.
- Cuando cambia un rol, entonces los permisos se actualizan.

---

### HU-02.2
**Como** usuario técnico  
**Quiero** tener acceso solo a módulos ambientales  
**Para** evitar modificar información administrativa  

**Criterios de Aceptación:**
- Dado un usuario técnico, cuando inicia sesión, entonces solo ve módulos permitidos.
- Si intenta acceder a otro módulo, entonces se le deniega acceso.

---

## Auditoría

### HU-03.1
**Como** auditor  
**Quiero** visualizar el registro de acciones  
**Para** garantizar transparencia  

**Criterios de Aceptación:**
- Cuando se realiza una acción, entonces se registra usuario, fecha y hora.
- Cuando el auditor consulta, entonces visualiza los registros.

---

## Monitoreo Ambiental

### HU-04.1
**Como** técnico de calidad del aire  
**Quiero** registrar puntos con coordenadas  
**Para** analizar contaminación  

**Criterios de Aceptación:**
- Cuando registra coordenadas, entonces se guardan correctamente.
- Cuando consulta el mapa, entonces visualiza el punto.

---

### HU-04.2
**Como** técnico de agua  
**Quiero** registrar puntos en ríos o lagunas  
**Para** evaluar calidad hídrica  

**Criterios de Aceptación:**
- Cuando registra datos, entonces se almacenan correctamente.

---

### HU-04.3
**Como** técnico de residuos  
**Quiero** registrar puntos de control  
**Para** monitorear residuos  

**Criterios de Aceptación:**
- Cuando registra un punto, entonces queda guardado en el sistema.

---

### HU-04.4
**Como** técnico de ruido  
**Quiero** registrar mediciones acústicas  
**Para** monitorear contaminación sonora  

**Criterios de Aceptación:**
- Cuando registra datos, entonces se guardan correctamente.

---

### HU-04.5
**Como** técnico vehicular  
**Quiero** registrar puntos móviles  
**Para** controlar emisiones  

**Criterios de Aceptación:**
- Cuando registra medición, entonces se almacena correctamente.

---

### HU-04.6
**Como** analista ambiental  
**Quiero** visualizar puntos en mapa  
**Para** analizar distribución  

**Criterios de Aceptación:**
- Cuando accede al mapa, entonces visualiza todos los puntos.
- Cuando filtra, entonces el mapa se actualiza.

---

## Datos Ambientales

### HU-05.1
**Como** técnico de aire  
**Quiero** cargar datos de contaminantes  
**Para** calcular ICA  

**Criterios de Aceptación:**
- Cuando ingresa datos, entonces el sistema los valida y guarda.

---

### HU-05.2
**Como** técnico de agua  
**Quiero** ingresar DBO y DQO  
**Para** evaluar calidad  

**Criterios de Aceptación:**
- Cuando ingresa datos, entonces se almacenan correctamente.

---

### HU-05.3
**Como** técnico de residuos  
**Quiero** registrar pesaje  
**Para** controlar volúmenes  

**Criterios de Aceptación:**
- Cuando registra datos, entonces se guardan correctamente.

---

### HU-05.4
**Como** técnico de ruido  
**Quiero** registrar decibeles  
**Para** monitorear contaminación  

**Criterios de Aceptación:**
- Cuando registra medición, entonces se almacena.

---

### HU-05.5
**Como** técnico vehicular  
**Quiero** registrar gases  
**Para** evaluar contaminación  

**Criterios de Aceptación:**
- Cuando registra datos, entonces se guardan correctamente.

---

### HU-05.6
**Como** analista  
**Quiero** cálculo automático de indicadores  
**Para** evitar errores  

**Criterios de Aceptación:**
- Cuando se ingresan datos, entonces el sistema calcula indicadores automáticamente.

---

## Históricos

### HU-06.1
**Como** planificador  
**Quiero** consultar datos históricos  
**Para** analizar tendencias  

**Criterios de Aceptación:**
- Cuando consulta datos, entonces se muestran correctamente.

---

## Reportes

### HU-07.1 a HU-07.5
**Como** jefe de área  
**Quiero** generar reportes  
**Para** analizar información  

**Criterios de Aceptación:**
- Cuando genera reporte, entonces los datos son correctos.
- Cuando aplica filtros, entonces se reflejan en el reporte.

---

### HU-07.6
**Como** analista  
**Quiero** visualizar gráficos  
**Para** analizar datos  

**Criterios de Aceptación:**
- Cuando accede, entonces visualiza gráficos correctos.

---

## Consulta Pública

### HU-08.1
**Como** ciudadano  
**Quiero** consultar información sin registrarme  
**Para** informarme  

**Criterios de Aceptación:**
- Cuando accede, entonces visualiza información pública.

---

## Integración

### HU-09.1
**Como** encargado  
**Quiero** sincronizar con SIGIR  
**Para** mantener datos actualizados  

**Criterios de Aceptación:**
- Cuando sincroniza, entonces los datos se actualizan correctamente.

---

## Mapas

### HU-10.1
**Como** analista  
**Quiero** filtrar mapas  
**Para** analizar datos  

**Criterios de Aceptación:**
- Cuando aplica filtros, entonces el mapa se actualiza.

---

## Exportación

### HU-11.1
**Como** técnico  
**Quiero** exportar reportes  
**Para** compartir información  

**Criterios de Aceptación:**
- Cuando exporta, entonces se genera archivo PDF/Excel.

---

## Ciudadano

### HU-12.1
**Como** ciudadano  
**Quiero** registrar solicitudes  
**Para** pedir inspecciones  

**Criterios de Aceptación:**
- Cuando registra solicitud, entonces se guarda correctamente.

---

## Notificaciones

### HU-13.1
**Como** usuario  
**Quiero** recibir notificaciones  
**Para** estar informado  

**Criterios de Aceptación:**
- Cuando ocurre evento, entonces recibe notificación.

---

## Dashboard

### HU-14.1
**Como** secretario  
**Quiero** ver indicadores  
**Para** tomar decisiones  

**Criterios de Aceptación:**
- Cuando accede, entonces visualiza indicadores actualizados.

---

## Imágenes

### HU-15.1
**Como** técnico  
**Quiero** optimizar imágenes  
**Para** mejorar rendimiento  

**Criterios de Aceptación:**
- Cuando sube imagen, entonces se comprime automáticamente.

---

## Roadmap

### HU-16.1
**Como** gestor  
**Quiero** documentar app futura  
**Para** planificación  

**Criterios de Aceptación:**
- Existe documento del roadmap.

---

## Requerimientos No Funcionales

### RNF-01 – Seguridad (Hashing de contraseñas)
**Como** encargado de seguridad  
**Quiero** proteger las contraseñas mediante hashing  
**Para** evitar accesos no autorizados  

**Criterios de Aceptación:**
- Dado que un usuario se registra, cuando guarda su contraseña, entonces se almacena en formato hash.
- Dado un intento de acceso a la base de datos, cuando se visualizan contraseñas, entonces no son legibles.
- Dado un inicio de sesión, cuando el usuario ingresa su contraseña, entonces el sistema valida mediante hashing.

---

### RNF-02 – Rendimiento
**Como** usuario  
**Quiero** consultas rápidas  
**Para** mejorar la experiencia de uso  

**Criterios de Aceptación:**
- Dado que el sistema tiene hasta 10,000 registros, cuando se realiza una consulta, entonces responde en menos de 1 segundo.
- Dado múltiples usuarios concurrentes, cuando acceden al sistema, entonces el rendimiento se mantiene estable.

---

### RNF-03 – Compatibilidad (Responsive)
**Como** usuario móvil  
**Quiero** usar el sistema desde cualquier dispositivo  
**Para** acceder sin limitaciones  

**Criterios de Aceptación:**
- Dado que el usuario accede desde un celular, cuando navega, entonces la interfaz se adapta correctamente.
- Dado diferentes tamaños de pantalla, cuando visualiza el sistema, entonces no hay errores de diseño.

---

## Requerimientos DevOps

### DEV-01 – Contenerización con Docker
**Como** ingeniero DevOps  
**Quiero** ejecutar el sistema en contenedores Docker  
**Para** facilitar despliegue y portabilidad  

**Criterios de Aceptación:**
- Dado el código del sistema, cuando se ejecuta Docker, entonces la aplicación inicia correctamente.
- Dado un entorno nuevo, cuando se despliega el contenedor, entonces funciona sin configuraciones adicionales.

---

### DEV-02 – Ambiente de Staging
**Como** equipo de desarrollo  
**Quiero** probar el sistema en un entorno de staging  
**Para** validar antes de producción  

**Criterios de Aceptación:**
- Dado un cambio en el sistema, cuando se despliega, entonces se refleja en staging.
- Dado pruebas realizadas, cuando se detectan errores, entonces no afectan producción.

---

### DEV-03 – Integración Continua (CI/CD)
**Como** desarrollador  
**Quiero** usar pipelines CI/CD  
**Para** automatizar pruebas y despliegues  

**Criterios de Aceptación:**
- Dado un commit en el repositorio, cuando se realiza push, entonces se ejecuta automáticamente el pipeline.
- Dado fallos en el código, cuando se ejecuta el pipeline, entonces se notifica el error.

---

### DEV-04 – Pruebas de Seguridad (Pentesting)
**Como** equipo de seguridad  
**Quiero** realizar pruebas de penetración  
**Para** detectar vulnerabilidades  

**Criterios de Aceptación:**
- Dado el sistema desplegado, cuando se ejecutan pruebas de seguridad, entonces se identifican vulnerabilidades.
- Dado vulnerabilidades detectadas, cuando se corrigen, entonces el sistema mejora su seguridad.
