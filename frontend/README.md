# SMIA - Sistema Municipal de Información Ambiental

Plataforma para la alcaldía de La Paz. Gestión de datos ambientales: aire, agua, residuos, ruido y emisiones vehiculares.

## Stack

- Frontend: Angular 17+, TailwindCSS, Leaflet
- Backend: Django + Django REST Framework + GeoDjango
- Base de datos: PostgreSQL + PostGIS
- Despliegue: Docker + Docker Compose

## Requisitos

- Docker Desktop
- Node.js 18+
- Python 3.10+

## Levantar el proyecto

```bash
docker compose up -d --build
docker compose ps