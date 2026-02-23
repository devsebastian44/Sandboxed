# Arquitectura: Sandboxed Malware Analysis

Sandboxed es una herramienta de orquestación de análisis estático diseñada para proporcionar un entorno seguro y estructurado para examinar archivos sospechosos.

## Flujo de Trabajo

1. **Entrada**: Una ruta de archivo proporcionada por el usuario.
2. **Validación**: La herramienta verifica la existencia y el tipo del archivo.
3. **Ejecución**: Según el tipo de archivo (Windows, Linux, Office, PDF), se invocan herramientas específicas de análisis estático.
4. **Captura de Datos**: La salida estándar y los errores de las herramientas se capturan y se guardan en el directorio `results/`.
5. **Revisión**: El usuario puede revisar los resultados directamente en la CLI o examinando los logs generados.

## Componentes

- **src/sandbox.py**: Lógica principal de orquestación.
- **scripts/setup.sh**: Preparación del entorno e instalación de herramientas.
- **diagrams/**: Representaciones visuales del flujo del sistema.
- **results/**: (Ignorado por Git) Resultados de análisis locales.
