# Sandboxed: Entorno Profesional de Análisis de Malware

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![GitLab](https://img.shields.io/badge/GitLab-Repository-orange?logo=gitlab)
![License](https://img.shields.io/badge/License-GPL--3.0-red)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![Malware Analysis](https://img.shields.io/badge/Type-An%C3%A1lisis%20de%20Malware-darkred)
![Security](https://img.shields.io/badge/Security-Investigaci%C3%B3n-critical)

**Sandboxed** es una herramienta de orquestación de análisis estático orientada a DevSecOps. Proporciona un entorno estructurado, aislado y ético para que investigadores y profesionales de seguridad examinen archivos sospechosos (ejecutables de Windows, binarios de Linux y documentos) utilizando herramientas estándar de la industria.

---

## 🎯 Objetivo del Proyecto

Este repositorio está diseñado para demostrar un enfoque profesional en la investigación de malware. Se centra en la automatización, documentación técnica clara y la separación de un portafolio público (GitHub) de un laboratorio de investigación totalmente funcional (GitLab).

## ⚖️ Propósito Ético y Educativo

Esta herramienta es estrictamente para **investigación educativa y defensiva**.
- **Advertencia de Uso**: La ejecución de payloads o el análisis de malware SOLAMENTE debe realizarse en máquinas virtuales aisladas.
- **Responsabilidad**: El usuario es el único responsable del cumplimiento legal y la seguridad.

## 🚀 Instalación y Acceso

> [!IMPORTANT]
> El repositorio completo con todo el código funcional está disponible en **GitLab** para acceso completo.

https://gitlab.com/group-cybersecurity-lab/sandboxed.git


---

## 🏗️ Estructura del Repositorio

- **src/**: Lógica central de orquestación en Python.
- **scripts/**: Scripts de instalación y configuración del entorno.
- **docs/**: Documentación técnica detallada (`ARCHITECTURE.md`).
- **diagrams/**: Flujo del sistema y arquitectura visual (`FLOW.md`).
- **tests/**: Verificaciones automáticas y controles de seguridad.
- **configs/**: Plantillas de configuración.

---

## 🚀 Empezando

### 📋 Prerrequisitos

- OS: Linux (Ubuntu/Debian recomendado)
- Python 3.8+
- Privilegios de root para la instalación de herramientas.

### 🛠️ Instalación

```bash
git clone https://github.com/bl4ck44/Sandboxed.git
cd Sandboxed
sudo bash scripts/setup.sh
```

### 🔍 Uso

```bash
python3 src/sandbox.py
```

---

## 🔄 Integración DevSecOps

### Flujo GitLab ➔ GitHub

El proyecto implementa una estrategia de **Seguridad por Diseño** que separa el laboratorio funcional del portafolio arquitectónico:

### GitLab (Laboratorio Público Completo)

El repositorio de GitLab funciona como **laboratorio público** que contiene:
- **Código Fuente Completo**: Toda la lógica funcional de análisis de malware
- **Pipelines CI/CD**: Integración continua con linting (*flake8*, *shellcheck*), análisis SAST (*bandit*) y pruebas automatizadas (*pytest*)
- **Suite de Pruebas Integral**: Tests unitarios, funcionales y de integración
- **Herramientas Especializadas**: Configuraciones avanzadas y payloads de análisis
- **Documentación Técnica**: Manuales de operación y arquitectura detallada

### GitHub (Portafolio Arquitectónico)

La versión pública en GitHub sirve como **portafolio profesional** que demuestra:
- **Arquitectura del Sistema**: Estructura y diseño del entorno sandboxed
- **Mejores Prácticas DevSecOps**: Estrategias de seguridad y automatización
- **Documentación de Referencia**: Guías técnicas y flujos de trabajo
- **Perfil Profesional**: Presentación limpia sin funcionalidades críticas

### Script de Sincronización

El script `scripts/sync_to_github.sh` gestiona la publicación sanitizada:
1. **Validación Automática**: Ejecuta pipelines completos en GitLab
2. **Sanitización Controlada**: Remueve código sensible y configuraciones internas
3. **Sincronización Segura**: Publica solo arquitectura y documentación en GitHub

---

## 🛠️ Herramientas Integradas

| Categoría | Herramientas |
| :--- | :--- |
| **Windows** | `manalyze`, `peframe`, `pestr`, `flarestrings`, `floss` |
| **Linux** | `trid`, `exiftool`, `cutter` |
| **Docs/PDF** | `pcodedmp`, `olevba`, `xlmdeobfuscator`, `pdfextract`, `pdfresurrect` |
