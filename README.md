## Sandboxed

<p align="center">
  <img src="./Img/Logo.png" height="300px" width="350px">
</p>

Un **sandbox** es un entorno de pruebas aislado en el que se pueden ejecutar aplicaciones o programas sin afectar el sistema operativo subyacente.  
Este repositorio te servirá para **analizar malware en un entorno seguro**, ya que incluye herramientas útiles y fáciles de usar.

---

## ⚙️ Requisitos

- Sistema operativo: Linux (Ubuntu recomendado)
- Python 3.8 o superior
- Permisos de administrador para ejecutar `setup.sh`

---

## 🚀 Instalación

Clona el repositorio y accede al directorio:

```bash
git clone https://github.com/bl4ck44/Sandboxed.git
cd Sandboxed
```

Configura el entorno:

```bash
chmod +x setup.sh
sudo bash setup.sh
```

---

## ▶️ Uso

Ejecuta el script principal:

```bash
python3 sandbox.py
```

---

## 🛠️ Contenido de herramientas

### Analizar ejecutables de Windows
- **Propiedades estáticas:** manalyze, peframe  
- **Strings y Deofuscación:** pestr, flarestrings, floss  

### Binarios Linux de ingeniería inversa
- **Propiedades estáticas:** trid, exiftool  
- **Desmontar/Descompilar:** cutter  

### Examinar documentos sospechosos
- **Archivos de Microsoft Office:** pcodedmp, olevba, xlmdeobfuscator  
- **Archivos PDF:** pdfextract, pdfdecrypt, pdfresurrect  

---

## 📜 Licencia

Este proyecto está bajo la licencia GPL.  
Puedes usarlo libremente con fines educativos y de investigación.

---

## ⚠️ Aviso

Este script ha sido desarrollado únicamente con fines **educativos y de investigación en ciberseguridad**.  
El uso indebido de este material puede ser **ilegal**.  
No me responsabilizo del mal uso ni de los daños que puedan ocasionarse por su ejecución.
