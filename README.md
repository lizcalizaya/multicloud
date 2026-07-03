# EVA03 - Infraestructura MultiCloud con Seguridad y CI/CD

## Descripción

Aplicación web desarrollada en Django para demostrar una arquitectura MultiCloud segura, integrando servicios de AWS, OCI y Azure.

## Arquitectura solicitada

Usuario → GitHub Actions → App Web en AWS EC2 / VPC  
App Web → OCI Autonomous AI Database  
App Web → Azure Blob Storage  

## Componentes implementados

- Aplicación web Django.
- Login y panel protegido.
- Controles OWASP:
  - Protección CSRF.
  - Autenticación con login/logout.
  - Sesiones seguras.
  - Cabeceras de seguridad.
  - Validación de formularios.
- Azure Blob Storage integrado para carga, visualización y eliminación de archivos.
- Pipeline GitHub Actions base con etapa de build/test.

## Componentes pendientes

- AWS EC2/VPC: pendiente porque el laboratorio AWS se encuentra en proceso de limpieza o con restricción de permisos.
- OCI Autonomous Database: pendiente de wallet/base activa, ya que el wallet entregado genera error DPY-6001 / ORA-12514.

## Variables de entorno

El proyecto usa un archivo `.env`, no incluido en GitHub por seguridad.  
Se incluye `.env.example` como plantilla.

## Ejecución local

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver