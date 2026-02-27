# 1. Introducción y Contexto del Proyecto


**Equipo:** Génesis Apaza ·  Anel Quiroz  · Esmeralda Alegre · Eva Chino · Daynor Mamani  
**Fecha:** 26/02/2026 | **Versión:** 1.2


---


## 1.1 Antecedentes (TDR GAMLP — Proyecto Basura 0)
En el marco de las gestiones ante la **Agencia Sueca de Cooperación Internacional para el Desarrollo (ASDI)**, se consolidaron recursos para el Proyecto **"Basura 0"** en Bolivia, implementado por HELVETAS, SWISSCONTACT y AGUATUYA.


La Secretaría Municipal de Gestión Ambiental (SMGA) del GAMLP gestiona componentes de monitoreo con herramientas dispersas (Excel, papel). Por normativa legal, se requiere el diseño e implementación del **Sistema Municipal de Información Ambiental (SMIA)**.


## 1.2 Problema de Negocio
**Fragmentación, desorganización y falta de integración tecnológica** en la gestión de información ambiental del municipio de La Paz, lo que causa demoras en informes para el MMAyA, pérdida de datos por registros manuales y falta de transparencia ciudadana.


## 1.3 Objetivo Principal
Diseñar, desarrollar e implementar el Sistema Municipal de Información Ambiental (SMIA) para registrar, almacenar y gestionar información técnica para funcionarios del GAMLP, brindar información a la ciudadanía e integrarse al sistema nacional SIGIR.


---


## 1.4 Tabla de Stakeholders


| Rol | Nombre / Cargo | Nivel de Influencia | Expectativa Principal |
|-----|---------------|--------------------|-----------------------|
| **Cliente / Patrocinador** | Secretaría Municipal de Gestión Ambiental (SMGA) | Alto | Contar con un sistema funcional, integrado y seguro que cumpla el TDR en 90 días |
| **Cliente / Patrocinador** | Swisscontact — Proyecto Basura 0 | Alto | Cumplimiento de los objetivos del Proyecto "Basura 0" financiado por ASDI |
| **Cliente / Financiador** | ASDI — Agencia Sueca de Cooperación Internacional | Alto | Uso eficiente de recursos y cumplimiento de metas de gestión ambiental |
| **Usuario Interno** | Técnico de la SMGA (7 áreas de monitoreo) | Medio | Plataforma fácil para cargar datos desde campo, con formularios digitales que reemplacen el papel |
| **Usuario Interno** | Director de la SMGA | Alto | Reportes oficiales automáticos para el MMAyA. Dashboard de estado ambiental |
| **Usuario Externo** | Ciudadanía del Municipio de La Paz | Medio | Acceso transparente a información ambiental. Solicitar servicios sin trámites presenciales |
| **Usuario Externo** | Operadores de residuos y empresas de reciclaje | Medio | Registro digital simplificado y consulta de habilitación legal |
| **Autoridad Regulatoria** | MMAyA — Ministerio de Medio Ambiente y Agua | Alto | Integración con SIGIR (Ley N°755). Informes ambientales en formato oficial |
| **Supervisor del TDR** | Técnico designado por la SMGA | Alto | Verificar cumplimiento del TDR. Aprobar los 3 informes de entrega |
| **Equipo Técnico** | **Anel Quiroz** (Scrum Master)<br>**Génesis Apaza** (Product Owner)<br>**Eva Chino, Esmeralda Alegre, Daynor Mamani** (Developers) | Alto | **SM:** Asegurar Scrum y cumplimiento de Sprints en 90 días.<br>**PO:** Priorizar el Backlog y asegurar el valor para la SMGA.<br>**Devs:** Construir plataforma estable (Frontend, Backend, BD) cumpliendo la DoD. |
| **Mantenimiento (DevOps)** | Equipo TIC del GAMLP (UDIT) / Ingenieros DevOps | Medio | Gestionar el despliegue de la aplicación, garantizar la observabilidad (monitoreo de métricas/logs) y mantener la infraestructura operativa a largo plazo. |


### Fase B — Técnicas de Elicitación Aplicadas


| Técnica | Aplicación en el SMIA |
|---------|----------------------|
| **Análisis Documental** | Revisión del TDR oficial GAMLP, Ley N°755, REGAM (OM 152/2010), Normativa 337 GAMLP |
| **Entrevistas** | Reuniones con el Director de la SMGA y técnicos de cada área de monitoreo |
| **Observación (Shadowing)** | Acompañamiento en jornadas de campo de la Red Monica y monitoreo hídrico |
| **Prototipado** | Bocetos del mapa de monitoreo y formularios digitales validados con técnicos |


### Fase C — Clasificación
Ver documentos `02`, `03`  de este índice.


---


## Alcance del Sistema


**INCLUYE:** Módulo PAM (autenticación), 7 módulos ambientales, reportes PDF/Excel, portal ciudadano, integración SIGIR, migración de 5 años de datos históricos, documentación Normativa 337.


**EXCLUYE:** Aplicación móvil nativa (iOS/Android), sistema de cobros/multas, control de drones, gestión de nóminas del municipio.


---


## Marco Legal


| Norma | Relevancia para el SMIA |
|-------|------------------------|
| **Ley N° 755** | Integración obligatoria con SIGIR del MMAyA |
| **REGAM (OM 152/2010)** | El GAMLP debe contar con un sistema de información ambiental |
| **Normativa 337 GAMLP** | Estándar para documentación técnica de sistemas municipales |
| **Ley de Transparencia** | Acceso público a información ambiental gubernamental |


