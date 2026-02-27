# 03_Requerimientos_No_Funcionales_DevOps


## RNF-01 – Seguridad


**Categoría:** Seguridad  


**Descripción:**  
El sistema no debe almacenar contraseñas en texto plano. Todas las credenciales de usuario deben almacenarse utilizando algoritmos de hashing seguro como bcrypt o Argon2.


**Justificación:**  
Garantiza la protección de la información sensible de los usuarios y reduce el riesgo ante posibles ataques o accesos no autorizados.


**Métrica de Éxito:**  
- Verificación técnica de que las contraseñas están encriptadas en la base de datos.  
- Pruebas de autenticación exitosas sin exponer datos sensibles.


---


## RNF-02 – Rendimiento


**Categoría:** Performance  


**Descripción:**  
El sistema debe garantizar un tiempo de respuesta menor a 1 segundo en búsquedas que involucren hasta 10.000 registros.


**Justificación:**  
Asegura eficiencia en la consulta de información ambiental y mejora la experiencia del usuario.


**Métrica de Éxito:**  
- Pruebas de carga realizadas con 10.000 registros.  
- Tiempo de respuesta promedio menor a 1 segundo.


---


## RNF-03 – Compatibilidad


**Categoría:** Usabilidad / Compatibilidad  


**Descripción:**  
El sistema debe ser Web Responsive, permitiendo su correcta visualización y funcionamiento tanto en dispositivos móviles como en computadoras de escritorio.


**Justificación:**  
Facilita el acceso a la plataforma desde diferentes dispositivos y mejora la accesibilidad para usuarios internos y externos.


**Métrica de Éxito:**  
- Visualización correcta en navegadores modernos (Chrome, Firefox, Edge).  
- Adaptación automática del diseño según tamaño de pantalla.


