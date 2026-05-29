# DevSecOps Demo

Proyecto de prueba orientado a la implementación de prácticas DevSecOps dentro de un flujo de integración continua.

## Objetivo

Implementar controles básicos de seguridad durante el ciclo de desarrollo utilizando herramientas nativas de GitHub.

Actualmente se está trabajando en:

- Automatización de procesos mediante GitHub Actions.
- Gestión segura de credenciales con GitHub Secrets.
- Validaciones automáticas dentro del pipeline.
- Detección de configuraciones inseguras.

## Tecnologías utilizadas

- GitHub
- GitHub Actions
- GitHub Secrets
- Python 3.11

## Estructura del proyecto

```text
.
├── .github
│   └── workflows
│       └── devsecops.yml
├── security-check.py
└── README.md
```

## Pipeline implementado

El flujo actual se ejecuta automáticamente cuando se realiza un push o pull request al repositorio.

Las validaciones incluidas son:

- Verificación de acceso a secretos configurados en GitHub.
- Ejecución de pruebas de seguridad básicas.
- Revisión de posibles credenciales expuestas en el código.
- Generación de resultados de ejecución.

## Estado actual

En desarrollo.

Próximas mejoras:

- Escaneo de vulnerabilidades en dependencias.
- Integración con herramientas SAST.
- Reportes automáticos de seguridad.
- Despliegue automatizado.
