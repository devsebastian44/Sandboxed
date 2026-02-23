#!/bin/bash

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Directorio temporal para instalaciones
TEMP_DIR="/tmp/sandboxed_install"

# Manejador de interrupción
int_handler() {
    clear
    echo
    echo -e "${BOLD}[+] Saliendo...${NC}"
    echo
    exit 0
}

trap 'int_handler' INT

# Verificar si se ejecuta como root
if [ "$(id -u)" != "0" ]; then
   echo -e "${RED}[!] Este script debe ejecutarse como root (usando sudo)${NC}"
   exit 1
fi

# Función para mostrar banner
mostrar_banner() {
    clear
    echo
    echo -e "${GREEN}   _________                  .______.                           .___  ${NC}"
    echo -e "${GREEN}  /   _____/____    ____    __| _/\_ |__   _______  ___ ____   __| _/  ${NC}"
    echo -e "${GREEN}  \_____  \\__  \  /    \  / __ |  | __ \ /  _ \  \/  // __ \ / __ |   ${NC}"
    echo -e "${GREEN}  /        \/ __ \|   |  \/ /_/ |  | \_\ (  <_> >    <\  ___// /_/ |   ${NC}"
    echo -e "${GREEN} /_______  (____  /___|  /\____ |  |___  /\____/__/\_ \\___  >____ |   ${NC}"
    echo -e "${GREEN}         \/     \/     \/      \/      \/            \/    \/     \/   ${NC}"
    echo
}

# Función para verificar comando
verificar_comando() {
    local cmd=$1
    local nombre=$2
    if command -v "$cmd" >/dev/null 2>&1; then
        echo -e "${GREEN}[✓]${NC} $nombre"
        return 0
    else
        echo -e "${RED}[✗]${NC} $nombre"
        return 1
    fi
}

# Función para instalar con manejo de errores
instalar_con_verificacion() {
    local nombre=$1
    shift
    echo -e "\n${YELLOW}[*] Instalando $nombre...${NC}"
    if "$@"; then
        echo -e "${GREEN}[✓] $nombre instalado correctamente${NC}"
        return 0
    else
        echo -e "${RED}[✗] Error al instalar $nombre${NC}"
        return 1
    fi
}

# FUNCIÓN: Comprobar requisitos
Comprobar() {
    echo -e "\n${BOLD}=== VERIFICACIÓN DE HERRAMIENTAS ===${NC}\n"
    
    echo -e "${BOLD}Análisis de Ejecutables Windows:${NC}"
    verificar_comando "manalyze" "Manalyze"
    verificar_comando "peframe" "PEframe"
    verificar_comando "pestr" "pestr"
    verificar_comando "floss" "FLOSS"
    verificar_comando "flarestrings" "FLARE strings"
    
    echo -e "\n${BOLD}Análisis de Binarios Linux:${NC}"
    verificar_comando "trid" "TrID"
    verificar_comando "exiftool" "ExifTool"
    verificar_comando "cutter" "Cutter"
    
    echo -e "\n${BOLD}Análisis de Documentos:${NC}"
    verificar_comando "pcodedmp" "pcodedmp"
    verificar_comando "olevba" "olevba"
    verificar_comando "xlmdeobfuscator" "XLMMacroDeobfuscator"
    verificar_comando "pdfextract" "pdfextract"
    verificar_comando "pdfresurrect" "pdfresurrect"
    
    echo
}

# INSTALADORES INDIVIDUALES

instalar_manalyze() {
    if command -v manalyze >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] Manalyze ya está instalado${NC}"
        return 0
    fi
    
    echo -e "${YELLOW}[*] Instalando dependencias de Manalyze...${NC}"
    apt-get update
    apt-get install -y libboost-regex-dev libboost-program-options-dev \
                       libboost-system-dev libboost-filesystem-dev \
                       libssl-dev build-essential cmake git
    
    mkdir -p "$TEMP_DIR"
    cd "$TEMP_DIR" || return 1
    
    echo -e "${YELLOW}[*] Clonando repositorio...${NC}"
    if git clone https://github.com/JusticeRage/Manalyze.git; then
        cd Manalyze || return 1
        
        echo -e "${YELLOW}[*] Compilando Manalyze...${NC}"
        if cmake . && make -j"$(nproc)"; then
            echo -e "${YELLOW}[*] Instalando Manalyze...${NC}"
            make install
            cd "$HOME" || exit
            echo -e "${GREEN}[✓] Manalyze instalado correctamente${NC}"
            return 0
        else
            echo -e "${RED}[✗] Error al compilar Manalyze${NC}"
            return 1
        fi
    else
        echo -e "${RED}[✗] Error al clonar repositorio${NC}"
        return 1
    fi
}

instalar_peframe() {
    if command -v peframe >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] PEframe ya está instalado${NC}"
        return 0
    fi
    
    apt-get install -y git python3-pip libreadline-dev
    pip3 install peframe
    echo -e "${GREEN}[✓] PEframe instalado${NC}"
}

instalar_pestr() {
    if command -v pestr >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] pestr ya está instalado${NC}"
        return 0
    fi
    
    apt-get install -y pev
    echo -e "${GREEN}[✓] pestr instalado${NC}"
}

instalar_floss() {
    if command -v floss >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] FLOSS ya está instalado${NC}"
        return 0
    fi
    
    echo -e "${YELLOW}[*] Descargando FLOSS...${NC}"
    wget -q https://github.com/mandiant/flare-floss/releases/latest/download/floss-linux -O /usr/local/bin/floss
    chmod +x /usr/local/bin/floss
    echo -e "${GREEN}[✓] FLOSS instalado${NC}"
}

instalar_flarestrings() {
    if command -v flarestrings >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] FLARE strings ya está instalado${NC}"
        return 0
    fi
    
    pip3 install flare-strings
    echo -e "${GREEN}[✓] FLARE strings instalado${NC}"
}

instalar_trid() {
    if command -v trid >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] TrID ya está instalado${NC}"
        return 0
    fi
    
    mkdir -p /opt/trid
    cd /opt/trid || return 1
    
    wget -q https://mark0.net/download/trid_linux_64.zip
    unzip -q trid_linux_64.zip
    chmod +x trid
    ln -sf /opt/trid/trid /usr/local/bin/trid
    
    # Descargar definiciones
    wget -q https://mark0.net/download/triddefs.zip
    unzip -q triddefs.zip
    
    echo -e "${GREEN}[✓] TrID instalado${NC}"
}

instalar_exiftool() {
    if command -v exiftool >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] ExifTool ya está instalado${NC}"
        return 0
    fi
    
    apt-get install -y libimage-exiftool-perl
    echo -e "${GREEN}[✓] ExifTool instalado${NC}"
}

instalar_cutter() {
    if command -v cutter >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] Cutter ya está instalado${NC}"
        return 0
    fi
    
    echo -e "${YELLOW}[*] Instalando Cutter (esto puede tardar)...${NC}"
    apt-get install -y cutter
    echo -e "${GREEN}[✓] Cutter instalado${NC}"
}

instalar_pcodedmp() {
    if command -v pcodedmp >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] pcodedmp ya está instalado${NC}"
        return 0
    fi
    
    pip3 install pcodedmp
    echo -e "${GREEN}[✓] pcodedmp instalado${NC}"
}

instalar_olevba() {
    if command -v olevba >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] olevba ya está instalado${NC}"
        return 0
    fi
    
    pip3 install oletools
    echo -e "${GREEN}[✓] olevba instalado${NC}"
}

instalar_xlmdeobfuscator() {
    if command -v xlmdeobfuscator >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] XLMMacroDeobfuscator ya está instalado${NC}"
        return 0
    fi
    
    pip3 install XLMMacroDeobfuscator
    echo -e "${GREEN}[✓] XLMMacroDeobfuscator instalado${NC}"
}

instalar_pdfextract() {
    if command -v pdfextract >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] pdfextract ya está instalado${NC}"
        return 0
    fi
    
    pip3 install pdfextract
    echo -e "${GREEN}[✓] pdfextract instalado${NC}"
}

instalar_pdfresurrect() {
    if command -v pdfresurrect >/dev/null 2>&1; then
        echo -e "${GREEN}[✓] pdfresurrect ya está instalado${NC}"
        return 0
    fi
    
    mkdir -p "$TEMP_DIR"
    cd "$TEMP_DIR" || return 1
    
    if git clone https://github.com/enferex/pdfresurrect.git; then
        cd pdfresurrect || return 1
        ./configure --prefix=/usr/local
        make
        make install
        cd "$HOME" || exit
        echo -e "${GREEN}[✓] pdfresurrect instalado${NC}"
    else
        echo -e "${RED}[✗] Error al clonar pdfresurrect${NC}"
        return 1
    fi
}

# FUNCIÓN: Instalar todos los requisitos
Instalar_Todo() {
    echo -e "\n${BOLD}=== INSTALACIÓN DE HERRAMIENTAS ===${NC}\n"
    
    # Actualizar sistema
    echo -e "${YELLOW}[*] Actualizando sistema...${NC}"
    apt-get update
    
    # Instalar herramientas
    instalar_pestr
    instalar_exiftool
    instalar_pcodedmp
    instalar_olevba
    instalar_xlmdeobfuscator
    instalar_pdfextract
    instalar_flarestrings
    instalar_peframe
    instalar_trid
    instalar_floss
    instalar_pdfresurrect
    instalar_cutter
    instalar_manalyze
    
    # Limpiar archivos temporales
    echo -e "\n${YELLOW}[*] Limpiando archivos temporales...${NC}"
    rm -rf "$TEMP_DIR"
    
    echo -e "\n${GREEN}[✓] Instalación completada${NC}"
    echo -e "${YELLOW}[!] Algunas herramientas pueden requerir configuración adicional${NC}"
}

# FUNCIÓN: Instalar requisitos selectivamente
Instalar_Selectivo() {
    echo -e "\n${BOLD}=== INSTALACIÓN SELECTIVA ===${NC}\n"
    echo "[1] Herramientas Windows (manalyze, peframe, pestr, floss, flarestrings)"
    echo "[2] Herramientas Linux (trid, exiftool, cutter)"
    echo "[3] Herramientas Documentos (pcodedmp, olevba, xlmdeobfuscator, pdfextract, pdfresurrect)"
    echo "[4] Todo"
    echo
    read -r -p "$(echo -e "${BOLD}[+] Seleccione categoría: ${NC}")" categoria
    
    case $categoria in
        1)
            instalar_manalyze
            instalar_peframe
            instalar_pestr
            instalar_floss
            instalar_flarestrings
            ;;
        2)
            instalar_trid
            instalar_exiftool
            instalar_cutter
            ;;
        3)
            instalar_pcodedmp
            instalar_olevba
            instalar_xlmdeobfuscator
            instalar_pdfextract
            instalar_pdfresurrect
            ;;
        4)
            Instalar_Todo
            ;;
        *)
            echo -e "${RED}[!] Opción inválida${NC}"
            ;;
    esac
}

# MENÚ PRINCIPAL
while true; do
    mostrar_banner
    echo -e "${BOLD}[1]${NC} Comprobar requisitos"
    echo -e "${BOLD}[2]${NC} Instalar todos los requisitos"
    echo -e "${BOLD}[3]${NC} Instalación selectiva"
    echo -e "${BOLD}[4]${NC} Salir"
    echo
    
    read -r -p "$(echo -e "${BOLD}[+] Seleccione una opción: ${NC}")" opcion
    
    case $opcion in
        1)
            Comprobar
            read -r -p "$(echo -e "\n${BOLD}Presione Enter para continuar...${NC}")"
            ;;
        2)
            Instalar_Todo
            read -r -p "$(echo -e "\n${BOLD}Presione Enter para continuar...${NC}")"
            ;;
        3)
            Instalar_Selectivo
            read -r -p "$(echo -e "\n${BOLD}Presione Enter para continuar...${NC}")"
            ;;
        4)
            clear
            echo
            echo -e "${BOLD}[+] Adiós${NC}"
            echo
            exit 0
            ;;
        *)
            echo -e "${RED}[!] Opción inválida${NC}"
            sleep 1
            ;;
    esac
done