
# 1. Introducción y Contexto del Proyecto

**Equipo:** Génesis Apaza · Esmeralda Alegre · Anel Quiroz · Eva Chino · Daynor Mamani  
**Fecha:** 19/02/2026 | **Versión:** 1.0

---

## ¿Qué es un Requerimiento?

Es una condición o capacidad que debe cumplir el sistema para satisfacer un contrato, estándar, especificación u otro documento formalmente impuesto. Describe **QUÉ** debe hacer el sistema, no **CÓMO** debe implementarse.

---

## Antecedentes (TDR GAMLP — Proyecto Basura 0)

En el marco de las gestiones ante la **Agencia Sueca de Cooperación Internacional para el Desarrollo (ASDI)**, se consolidaron recursos para el Proyecto **"Basura 0"** en Bolivia, implementado por **HELVETAS SWISS INTERCOOPERATION, SWISSCONTACT y AGUATUYA**.

La **Secretaría Municipal de Gestión Ambiental (SMGA)** gestiona 7 componentes de monitoreo ambiental con herramientas dispersas (Excel, papel). No existe un sistema unificado para estructurar, publicar ni integrar esta información.

---

## Problema de Negocio

**Fragmentación, desorganización y falta de integración tecnológica** en la gestión de información ambiental del municipio de La Paz. Cada área de la SMGA trabaja con sus propias herramientas, causando:

- Demoras de semanas en la elaboración de informes para el MMAyA
- Pérdida de datos por registro manual en papel
- Falta de transparencia ambiental para la ciudadanía
- Incumplimiento potencial de la Ley N°755 (sin integración con SIGIR)

---

## Objetivo Principal

Registrar, almacenar, actualizar y gestionar la información ambiental del municipio de La Paz en una sola plataforma web, proporcionando datos técnicos a funcionarios del GAMLP e información general a la ciudadanía.

---

## Fases de Identificación

### Fase A — Contexto y Stakeholders
---

> **Nota clave:** El **CLIENTE** es quien paga y aprueba. El **USUARIO** es quien opera el sistema. Son diferentes personas con necesidades distintas. Un buen ingeniero satisface a ambos.

---

## Tabla de Stakeholders

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
| **Equipo Técnico** | Empresa consultora (equipo desarrollador) | Alto | Cumplir contrato en 90 días con la tecnología aprobada por el GAMLP |
| **Mantenimiento** | Equipo TIC del GAMLP (UDIT) | Medio | Implementar solución técnica estable que puedan mantener sin soporte externo |

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

