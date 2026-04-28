# 🔬 Sandboxed

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![REMnux](https://img.shields.io/badge/REMnux-Compatible-4EAA25?style=flat&logo=linux&logoColor=white)
![Bandit](https://img.shields.io/badge/SAST-Bandit-critical?style=flat&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat&logo=github-actions&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-red?style=flat&logo=gnu&logoColor=white)
![Type](https://img.shields.io/badge/Type-Malware%20Analysis-darkred?style=flat&logo=virustotal&logoColor=white)

---

## 🧠 Overview

> [!IMPORTANTE]
> **Aviso ético:** Este proyecto tiene fines exclusivamente educativos y éticos en materia de ciberseguridad. Las herramientas y técnicas descritas solo deben utilizarse en entornos de laboratorio aislados y con autorización expresa.

**Sandboxed** es un orquestador de análisis estático de malware en Python de grado profesional, diseñado para ejecutarse sobre entornos Linux especializados como **REMnux**. A través de un menú interactivo centralizado (`sandbox.py`), la herramienta encadena y ejecuta un conjunto de utilidades de análisis forense clasificadas por tipo de artefacto: ejecutables Windows (PE), binarios Linux y documentos ofimáticos/PDF.

El sistema genera informes de análisis en múltiples formatos (`.txt`, `.pdf`) y los almacena en un directorio de resultados aislado (`results/`), garantizando que ningún artefacto de análisis sea rastreado por Git. La arquitectura separa la lógica central de orquestación (`src/`), los scripts de instalación y payloads de prueba (`scripts/`), y las configuraciones personalizables por entorno (`configs/*.yaml`).

El proyecto sigue una estrategia **DevSecOps integral**: el repositorio contiene el código operativo completo, la documentación técnica y los diagramas de arquitectura, optimizado para la colaboración en entornos de investigación de ciberseguridad.

> ⚠️ **Uso Responsable:** Esta herramienta está diseñada exclusivamente para análisis forense en entornos aislados y controlados. El análisis de muestras reales de malware debe realizarse estrictamente en máquinas virtuales sin acceso a redes de producción.

---

## ⚙️ Features

- **Menú interactivo de orquestación** (`sandbox.py`) que permite seleccionar y encadenar herramientas de análisis según el tipo de artefacto a examinar
- **Análisis de ejecutables Windows (PE)** mediante herramientas especializadas: `manalyze`, `peframe`, `pestr`, `flarestrings` y `floss` para extracción de strings ofuscadas y análisis estructural
- **Análisis de binarios Linux** con `trid` (identificación de tipo de archivo), `exiftool` (metadatos) y `cutter` (desensamblado y análisis de control de flujo)
- **Análisis de documentos y PDFs** a través de `pcodedmp`, `olevba`, `xlmdeobfuscator` (macros ofuscadas), `pdfextract` y `pdfresurrect`
- **Salida de reportes en múltiples formatos**: `.txt` y `.pdf` generados automáticamente en el directorio `Results/` (excluido de Git)
- **Sistema de configuración YAML por entorno**: `configs/*.yaml` con plantillas de ejemplo versionadas (`*.example.yaml`) y configuraciones locales gitignoreadas
- **Script de instalación de dependencias** (`scripts/setup.sh`) que configura el entorno de herramientas con privilegios de root
- **Subdirectorio de payloads de prueba** (`scripts/payloads/`) con muestras controladas para validación del pipeline de análisis (excluido de Git)
- **Suite de pruebas y calidad**: Integración con `flake8`, `shellcheck`, `bandit` y `pytest` para asegurar la calidad y seguridad del código
- **Hooks de pre-commit**: Automatización de linting y SAST local antes de cada commit

---

## 🛠️ Tech Stack

### Lenguaje y entorno

| Componente | Tecnología | Propósito |
|---|---|---|
| Lenguaje principal | Python 3.8+ | Orquestación del menú y control del flujo de análisis |
| Scripting | Bash (.sh) | Instalación de herramientas y sincronización entre repos |
| Configuración | YAML | Parámetros de entorno, rutas de herramientas y ajustes por perfil |
| Entorno base | REMnux (Linux) | Distribución Linux especializada en análisis de malware |

### Herramientas de análisis integradas

| Categoría | Herramientas | Función |
|---|---|---|
| **PE / Windows** | `manalyze` | Análisis heurístico de ejecutables PE |
| | `peframe` | Extracción de metadatos y secciones del binario |
| | `pestr` | Extracción de strings imprimibles en PE |
| | `flarestrings` | Extracción avanzada de strings (FLARE/Mandiant) |
| | `floss` | Deofuscación y extracción de strings dinámicas |
| **Linux / Binarios** | `trid` | Identificación del tipo de archivo por firma binaria |
| | `exiftool` | Lectura de metadatos embebidos en el archivo |
| | `cutter` | Desensamblado, análisis de CFG y análisis estático avanzado |
| **Documentos / PDF** | `pcodedmp` | Dump de código p-code VBA en documentos Office |
| | `olevba` | Extracción y análisis de macros VBA maliciosas |
| | `xlmdeobfuscator` | Deofuscación de macros XLM (Excel 4.0) |
| | `pdfextract` | Extracción de objetos embebidos en PDFs |
| | `pdfresurrect` | Recuperación de revisiones ocultas en PDFs |

### Pipeline de calidad y seguridad

| Herramienta | Propósito |
|---|---|
| `flake8` | Linting y verificación de estilo Python (PEP 8) |
| `shellcheck` | Análisis estático de scripts Bash |
| `bandit` | SAST — detección de patrones peligrosos en código Python |
| `pytest` | Suite de pruebas automatizadas unitarias y funcionales |

---

## 📦 Installation

### Requisitos previos

- **Sistema operativo:** Linux — REMnux (recomendado) o Ubuntu/Debian
- **Python:** 3.8 o superior
- **Privilegios:** root o sudo para instalación de herramientas del sistema

> 💡 Se recomienda ejecutar sobre una distribución **REMnux** donde la mayoría de herramientas de análisis ya están preinstaladas.

### Clonar el repositorio

```bash
git clone https://github.com/bl4ck44/Sandboxed.git
cd Sandboxed
```

### Configurar el entorno virtual Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Instalar herramientas de análisis del sistema

```bash
# Instalación automatizada con privilegios de root
sudo bash scripts/setup.sh
```

Este script instala y configura las herramientas de análisis listadas en el Tech Stack, verificando su disponibilidad en el PATH del sistema.

### Configurar el entorno local

```bash
# Copiar la plantilla de configuración y ajustar rutas locales
cp configs/settings.example.yaml configs/settings.yaml
nano configs/settings.yaml   # Editar rutas de herramientas si es necesario
```

### Ejecutar Pruebas Locales

```bash
# Ejecutar suite de pruebas con pytest
pytest tests/ -v

# Ejecutar linting y análisis de seguridad
flake8 src/
bandit -r src/
```

### Instalar herramientas de análisis estático (CI local)

```bash
pip install flake8 bandit pytest
apt install shellcheck
```

---

## ▶️ Usage

### Ejecutar el menú principal de análisis

```bash
python3 src/sandbox.py
```

Al iniciarse, `sandbox.py` presenta un menú interactivo que permite:

1. Seleccionar el **tipo de artefacto** a analizar (PE Windows / binario Linux / documento-PDF)
2. Especificar la **ruta del archivo** sospechoso
3. Seleccionar las **herramientas** a ejecutar (una o varias encadenadas)
4. Generar el **reporte de resultados** en `Results/` en formato `.txt` o `.pdf`

```
┌─────────────────────────────────────┐
│         SANDBOXED — Main Menu       │
│─────────────────────────────────────│
│  [1] Analyze PE / Windows Binary    │
│  [2] Analyze Linux Binary           │
│  [3] Analyze Document / PDF         │
│  [4] Settings & Configuration       │
│  [0] Exit                           │
└─────────────────────────────────────┘
```

### Ejemplo de flujo de análisis de un PE

```bash
# Iniciar el orquestador
python3 src/sandbox.py

# Seleccionar opción 1 (PE / Windows)
# Ingresar ruta: /home/analyst/samples/suspicious.exe
# Seleccionar herramientas: manalyze, peframe, floss
# El reporte se genera automáticamente en Results/suspicious_report.txt
```

### Ejecutar el pipeline de seguridad localmente

```bash
# Linting Python
flake8 src/

# Análisis SAST
bandit -r src/

# Linting de scripts Bash
shellcheck scripts/*.sh

# Suite de pruebas
pytest tests/ -v
```


---

## 📁 Project Structure

```
Sandboxed/
│
├── src/                          # Lógica central de orquestación
│   └── sandbox.py                # Punto de entrada — menú interactivo de análisis
│
├── scripts/                      # Automatización y utilidades
│   ├── setup.sh                  # Instalación de herramientas de análisis (requiere root)
│   └── payloads/                 # Muestras de prueba controladas [gitignoreado]
│
├── configs/                      # Configuraciones por entorno
│   ├── settings.example.yaml     # Plantilla pública de configuración (versionada)
│   └── settings.yaml             # Configuración local con rutas reales [gitignoreado]
│
├── tests/                        # Suite de pruebas pytest [gitignoreado]
│   └── test_*.py                 # Pruebas unitarias y funcionales de los módulos
│
├── docs/                         # Documentación técnica
│   └── ARCHITECTURE.md           # Manual de arquitectura del sistema
│
├── diagrams/                     # Representaciones visuales del sistema
│   └── FLOW.md                   # Diagrama de flujo del pipeline de análisis
│
├── Results/                      # Salida de reportes de análisis [gitignoreado]
│   └── *.txt / *.pdf             # Informes generados por cada sesión de análisis
│
├── .pre-commit-config.yaml       # Configuración de hooks pre-commit (Linting / SAST local)
├── Makefile                      # Automatización DevSecOps (make install, test, lint)
├── requirements.txt              # Gestión centralizada de dependencias en Python
├── .gitignore                    # Control estricto de artefactos y secretos
├── LICENSE                       # GNU General Public License v3.0
└── README.md                     # Documentación pública del portafolio
```

> **Nota de seguridad sobre `.gitignore`:** El archivo excluye explícitamente `Results/`, `*.txt`, `*.pdf`, `*.bin`, `tests/`, `scripts/payloads/`, `.env` y `configs/*.yaml`. Esto garantiza que ningún reporte de análisis, muestra de malware, variable de entorno sensible ni resultado forense sea expuesto accidentalmente en el repositorio público.

---

## 🔐 Security

### Contexto de uso responsable

**Sandboxed** implementa un enfoque de **análisis estático**, lo que significa que las muestras de malware nunca se ejecutan — solo se inspeccionan en reposo. Esto reduce significativamente el riesgo de infección accidental del entorno de análisis. Sin embargo, el manejo de muestras reales siempre requiere medidas adicionales de contención.

### Implicaciones técnicas

- **Análisis estático exclusivamente:** Las herramientas integradas (`peframe`, `manalyze`, `olevba`, etc.) operan sobre los binarios sin ejecutarlos, minimizando la superficie de exposición
- **Aislamiento de resultados:** El directorio `Results/` está explícitamente excluido de Git mediante `.gitignore`, evitando la filtración de informes forenses que podrían contener IoCs (Indicadores de Compromiso) sensibles
- **Payloads de prueba gitignoreados:** `scripts/payloads/` contiene muestras controladas para validar el pipeline, pero nunca se sincronizan al repositorio público
- **Configuraciones sensibles protegidas:** Las configuraciones locales (`configs/*.yaml`) con rutas absolutas del sistema están excluidas; solo las plantillas de ejemplo (`.example.yaml`) son versionadas
- **SAST en el flujo de trabajo:** `bandit` analiza el código Python del orquestador en busca de llamadas peligrosas como `subprocess.shell=True`, `eval` o `exec` para prevenir vulnerabilidades de inyección
- **REMnux como entorno base:** Al estar diseñado para REMnux, el sistema asume un entorno ya hardeneado y específicamente configurado para análisis forense

### Buenas prácticas de laboratorio

- Ejecutar **exclusivamente en máquinas virtuales** sin interfaces de red activas hacia redes de producción (modo host-only o NAT aislado)
- Utilizar **snapshots de VM** antes de iniciar cada sesión de análisis para restaurar el estado limpio
- Nunca copiar muestras de malware a sistemas anfitriones (host) — mantenerlas confinadas en la VM
- Destruir y regenerar el entorno de análisis periódicamente para evitar acumulación de residuos maliciosos
- Verificar siempre el hash (SHA-256) de las muestras antes de analizarlas para garantizar la integridad de la cadena de custodia forense

---


---

## 🚀 Roadmap

- [ ] **Análisis dinámico ligero** — Integración con entornos de ejecución controlada (cuckoo sandbox local) como capa opcional sobre el análisis estático actual
- [ ] **Generación de reportes PDF automáticos** — Templates estructurados con metadatos del artefacto, hashes, IoCs detectados y resumen ejecutivo
- [ ] **Soporte para archivos comprimidos y empaquetados** — Descompresión y análisis automático de `.zip`, `.7z` y archivos UPX-packed
- [ ] **Base de datos de resultados** — Almacenamiento estructurado (SQLite) de análisis previos para correlación y comparación entre muestras
- [ ] **Integración con VirusTotal API** — Consulta automática de hash SHA-256 contra la base de datos de VirusTotal para enriquecer el reporte
- [ ] **Perfil de configuración múltiple** — Soporte para perfiles YAML diferenciados por tipo de laboratorio (básico, intermedio, avanzado)
- [ ] **Interfaz web liviana** — Panel Flask/FastAPI opcional para gestión de análisis y visualización de reportes desde el navegador
- [ ] **Cobertura pytest ≥ 85%** — Expansión de la suite de pruebas con mocks de herramientas externas y pruebas de integración completas
- [ ] **Soporte para macOS (Apple Silicon)** — Compatibilidad con herramientas disponibles en Homebrew para análisis en entornos macOS ARM

---

## 📄 License

**GNU General Public License v3.0** — Ver [`LICENSE`](./LICENSE)

El código puede ser usado, modificado y distribuido bajo los términos de la GPL-3.0, con la obligación de mantener el código fuente disponible en distribuciones derivadas. Queda explícitamente prohibido el uso de este software fuera de entornos de investigación autorizados o con fines maliciosos.

---

---

## 🤝 Contributing

¡Las contribuciones son bienvenidas! Para mantener la calidad del proyecto, sigue estos pasos:

1. **Fork** el repositorio.
2. Crea una nueva rama para tu funcionalidad (`git checkout -b feature/amazing-feature`).
3. Realiza tus cambios y asegúrate de que pasen los tests (`pytest tests/`).
4. Haz commit de tus cambios siguiendo [Conventional Commits](https://www.conventionalcommits.org/).
5. Realiza un **Push** a la rama (`git push origin feature/amazing-feature`).
6. Abre un **Pull Request**.

## 👨‍💻 Author

**Sebastian** — [`@devsebastian44`](https://github.com/devsebastian44)

Investigador en ciberseguridad con especialización en análisis de malware, forense digital y automatización de pipelines DevSecOps. Este proyecto forma parte de un laboratorio educativo de ciberseguridad orientado a la investigación defensiva.

| Plataforma | Enlace |
|---|---|
| GitHub | [github.com/devsebastian44](https://github.com/devsebastian44) |


---

> *Este repositorio es un portafolio educativo de análisis de malware. Todo el contenido ha sido diseñado para su uso en entornos de laboratorio aislados, con fines exclusivamente defensivos y de investigación en ciberseguridad.*