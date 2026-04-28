import os
import subprocess  # nosec B404
import sys
import shlex
import yaml


def cargar_configuracion(ruta_config="configs/settings.yaml"):
    """Carga la configuración desde un archivo YAML"""
    config_default = {
        "general": {"results_dir": "results", "timeout_seconds": 300},
        "tools": {
            "manalyze": "manalyze", "peframe": "peframe", "pestr": "pestr",
            "flarestrings": "flarestrings", "floss": "floss", "trid": "trid",
            "exiftool": "exiftool", "cutter": "cutter", "pcodedmp": "pcodedmp",
            "olevba": "olevba", "xlmdeobfuscator": "xlmdeobfuscator",
            "pdfextract": "pdfextract", "pdfresurrect": "pdfresurrect"
        }
    }
    if os.path.exists(ruta_config):
        try:
            with open(ruta_config, "r", encoding="utf-8") as f:
                config_usuario = yaml.safe_load(f)
                if config_usuario:
                    # Mezclar con valores por defecto
                    for key in config_default:
                        if key in config_usuario:
                            config_default[key].update(config_usuario[key])
        except Exception as e:
            print(f"[!] Error al cargar configuración: {e}. Usando valores por defecto.")
    return config_default


CONFIG = cargar_configuracion()


def limpiar_pantalla():
    """Limpia la pantalla de forma multiplataforma"""
    if os.name == "nt":
        # cls is a shell internal in Windows, shell=True is required
        subprocess.run(["cls"], shell=True, check=False)  # nosec B602, B607
    else:
        # Using clear to reset terminal state
        subprocess.run(["clear"], check=False)  # nosec B603, B607


def crear_estructura_directorios():
    """Crea la estructura de directorios necesaria"""
    # Use relative path for results to stay within project root
    directorios = ["results", "results/PDF"]
    for directorio in directorios:
        if not os.path.exists(directorio):
            os.makedirs(directorio)


def mostrar_banner():
    """Muestra el banner de la aplicación"""
    print("")
    b1 = r"  _________                  .______.                           "
    b1 += r".___"
    b2 = r" /   _____/____    ____    __| _/\_ |__   _______  ___ ____   "
    b2 += r"__| _/"
    b3 = r" \_____  \\__  \  /    \  / __ |  | __ \ /  _ \  \/  // __ \ "
    b3 += r"/ __ | "
    b4 = r" /        \/ __ \|   |  \/ /_/ |  | \_\ (  <_> >    <\  ___// "
    b4 += r"/_/ | "
    b5 = r"/_______  (____  /___|  /\____ |  |___  /\____/__/\_ \\___  "
    b5 += r">____ | "
    b6 = r"        \/     \/     \/      \/      \/            \/    \/     "
    b6 += r"\/ "
    print("\033[91m" + b1 + "\033[0m")
    print("\033[91m" + b2 + "\033[0m")
    print("\033[91m" + b3 + "\033[0m")
    print("\033[91m" + b4 + "\033[0m")
    print("\033[91m" + b5 + "\033[0m")
    print("\033[91m" + b6 + "\033[0m")
    print("")


def ejecutar_comando(comando, nombre_archivo, directorio="results"):
    """Ejecuta un comando y guarda el resultado en un archivo"""
    try:
        dir_actual = os.getcwd()
        os.chdir(directorio)

        print(f"\n[*] Ejecutando: {comando}")
        print("[*] Esto puede tardar un momento...")

        # Shlex.split for safe command argument separation
        # shell=False (default) prevents shell injection
        # args are properly parsed by shlex to prevent injection
        args = shlex.split(comando)
        timeout = CONFIG["general"].get("timeout_seconds", 300)
        resultado = subprocess.run(
            args, capture_output=True, text=True, timeout=timeout, check=False
        )  # nosec B603

        salida = resultado.stdout + resultado.stderr

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(salida)

        print(f"[✓] Resultados guardados en: {directorio}/{nombre_archivo}")
        print("\n" + "=" * 60)
        print(salida[:2000])
        if len(salida) > 2000:
            print(f"\n... (ver archivo completo en {nombre_archivo})")
        print("=" * 60)

        os.chdir(dir_actual)
        return True

    except subprocess.TimeoutExpired:
        print("[!] El comando excedió el tiempo límite de 5 minutos")
        os.chdir(dir_actual)
        return False
    except FileNotFoundError:
        msg = "Error: Comando no encontrado. Asegúrate de instalarlo."
        print(f"[!] {msg}")
        os.chdir(dir_actual)
        return False
    except Exception as e:
        print(f"[!] Error al ejecutar comando: {e}")
        os.chdir(dir_actual)
        return False


def validar_archivo(ruta):
    """Valida que el archivo exista"""
    if not ruta or ruta.strip() == "":
        msg = "Error: No se especificó ningún archivo"
        print(f"[!] {msg}")
        return False
    if not os.path.exists(ruta):
        print(f"[!] Error: El archivo '{ruta}' no existe")
        return False
    if not os.path.isfile(ruta):
        print(f"[!] Error: '{ruta}' no es un archivo válido")
        return False
    return True


def pausar():
    """Pausa para que el usuario pueda leer los resultados"""
    input("\n[Presione Enter para continuar...]")


def menu_analisis_windows(archivo):
    """Menú para análisis de ejecutables Windows"""
    while True:
        print("\n" + "=" * 60)
        print("ANÁLISIS DE EJECUTABLES WINDOWS")
        print("=" * 60)
        print(f"Archivo: {archivo}")
        print("")
        print("[1] Propiedades estáticas")
        print("[2] Cadenas y desofuscación")
        print("[99] Volver al menú principal")

        msg = "\033[1m\n[+] Ingrese una opción: \033[0m"
        opcion = input(msg).strip()

        if opcion == "1":
            print("\n[1] Analizar con manalyze")
            print("[2] Analizar con peframe")
            print("[99] Volver")
            sub_opcion = input(msg).strip()

            if sub_opcion == "1":
                ejecutar_comando(f"{CONFIG['tools']['manalyze']} {archivo}", "manalyze.txt")
                pausar()
            elif sub_opcion == "2":
                ejecutar_comando(f"{CONFIG['tools']['peframe']} {archivo}", "peframe.txt")
                pausar()
            elif sub_opcion == "99":
                continue
            else:
                print("[!] Opción inválida")
                pausar()

        elif opcion == "2":
            print("\n[1] Analizar con pestr")
            print("[2] Analizar con flarestrings")
            print("[3] Analizar con floss")
            print("[99] Volver")
            sub_opcion = input(msg).strip()

            if sub_opcion == "1":
                ejecutar_comando(f"{CONFIG['tools']['pestr']} {archivo}", "pestr.txt")
                pausar()
            elif sub_opcion == "2":
                ejecutar_comando(f"{CONFIG['tools']['flarestrings']} {archivo}", "flarestrings.txt")
                pausar()
            elif sub_opcion == "3":
                ejecutar_comando(f"{CONFIG['tools']['floss']} {archivo}", "floss.txt")
                pausar()
            elif sub_opcion == "99":
                continue
            else:
                print("[!] Opción inválida")
                pausar()

        elif opcion == "99":
            break
        else:
            print("[!] Opción inválida")
            pausar()


def menu_analisis_linux(archivo):
    """Menú para análisis de binarios Linux"""
    while True:
        print("\n" + "=" * 60)
        print("ANÁLISIS DE BINARIOS LINUX")
        print("=" * 60)
        print(f"Archivo: {archivo}")
        print("")
        print("[1] Propiedades estáticas")
        print("[2] Desmontar o Descompilar")
        print("[99] Volver al menú principal")

        msg = "\033[1m\n[+] Ingrese una opción: \033[0m"
        opcion = input(msg).strip()

        if opcion == "1":
            print("\n[1] Analizar con trid")
            print("[2] Analizar con exiftool")
            print("[99] Volver")
            sub_opcion = input(msg).strip()

            if sub_opcion == "1":
                ejecutar_comando(f"{CONFIG['tools']['trid']} {archivo}", "trid.txt")
                pausar()
            elif sub_opcion == "2":
                ejecutar_comando(f"{CONFIG['tools']['exiftool']} {archivo}", "exiftool.txt")
                pausar()
            elif sub_opcion == "99":
                continue
            else:
                print("[!] Opción inválida")
                pausar()

        elif opcion == "2":
            print("\n[1] Analizar con cutter")
            print("[99] Volver")
            sub_opcion = input(msg).strip()

            if sub_opcion == "1":
                print(f"[*] Abriendo Cutter con el archivo: {archivo}")
                try:
                    # Application specific orchestration
                    subprocess.run(
                        [CONFIG['tools']['cutter'], archivo], check=False
                    )  # nosec B603, B607
                except FileNotFoundError:
                    print("[!] Error: Cutter no está instalado.")
                    pausar()
            elif sub_opcion == "99":
                continue
            else:
                print("[!] Opción inválida")
                pausar()

        elif opcion == "99":
            break
        else:
            print("[!] Opción inválida")
            pausar()


def menu_documentos(archivo):
    """Menú para análisis de documentos sospechosos"""
    while True:
        print("\n" + "=" * 60)
        print("ANÁLISIS DE DOCUMENTOS SOSPECHOSOS")
        print("=" * 60)
        print(f"Archivo actual: {archivo}")
        print("")
        print("[1] Archivos de Microsoft Office")
        print("[2] Archivos PDF")
        print("[3] Usar otro archivo")
        print("[99] Volver al menú principal")

        msg = "\033[1m\n[+] Ingrese una opción: \033[0m"
        opcion = input(msg).strip()

        if opcion == "1":
            print("\n[1] Analizar con pcodedmp")
            print("[2] Analizar con olevba")
            print("[3] Analizar con XLMMacroDeobfuscator (Excel)")
            print("[99] Volver")
            sub_opcion = input(msg).strip()

            if sub_opcion == "1":
                ejecutar_comando(f"{CONFIG['tools']['pcodedmp']} {archivo}", "pcodedmp.txt")
                pausar()
            elif sub_opcion == "2":
                ejecutar_comando(f"{CONFIG['tools']['olevba']} {archivo}", "olevba.txt")
                pausar()
            elif sub_opcion == "3":
                ejecutar_comando(
                    f"{CONFIG['tools']['xlmdeobfuscator']} --file {archivo}",
                    "XLMMacroDeobfuscator.txt"
                )
                pausar()
            elif sub_opcion == "99":
                continue
            else:
                print("[!] Opción inválida")
                pausar()

        elif opcion == "2":
            def_path = "results/PDF"
            prompt = f"[+] Directorio de salida (Enter para '{def_path}'): "
            destino = input("\033[1m\n" + prompt + "\033[0m").strip()
            if not destino:
                destino = def_path

            print("\n[1] Analizar con pdfextract")
            print("[2] Analizar con pdfresurrect")
            print("[99] Volver")
            sub_opcion = input(msg).strip()

            if sub_opcion == "1":
                cmd = f"{CONFIG['tools']['pdfextract']} -afjms {archivo} -d {destino}"
                ejecutar_comando(cmd, "pdfextract.txt", "results/PDF")
                pausar()
            elif sub_opcion == "2":
                ejecutar_comando(f"{CONFIG['tools']['pdfresurrect']} {archivo}", "pdfresurrect.txt")
                pausar()
            elif sub_opcion == "99":
                continue
            else:
                print("[!] Opción inválida")
                pausar()

        elif opcion == "3":
            prompt = "[+] Ingresa la ubicación del nuevo archivo: "
            nuevo_archivo = input("\033[1m\n" + prompt + "\033[0m").strip()
            if validar_archivo(nuevo_archivo):
                archivo = nuevo_archivo
                print(f"[✓] Usando temporalmente: {archivo}")
                pausar()
            else:
                print("[!] Archivo no válido, manteniendo el anterior")
                pausar()

        elif opcion == "99":
            break
        else:
            print("[!] Opción inválida")
            pausar()


def menu_principal(archivo_global):
    """Menú principal de la aplicación"""
    while True:
        limpiar_pantalla()
        mostrar_banner()
        print("=" * 60)
        print("MENÚ PRINCIPAL - SANDBOXED")
        print("=" * 60)
        print(f"📁 Archivo actual: \033[1m{archivo_global}\033[0m")
        print("")
        print("[1] Analizar ejecutables de Windows")
        print("[2] Binarios Linux de ingeniería inversa")
        print("[3] Examinar documentos sospechosos")
        print("[4] Cambiar archivo principal")
        print("[5] Salir")

        msg = "\033[1m\n[+] Ingrese una opción: \033[0m"
        opcion = input(msg).strip()

        if opcion == "":
            print("[!] Por favor ingrese una opción")
            pausar()
        elif opcion == "1":
            if validar_archivo(archivo_global):
                menu_analisis_windows(archivo_global)
        elif opcion == "2":
            if validar_archivo(archivo_global):
                menu_analisis_linux(archivo_global)
        elif opcion == "3":
            if validar_archivo(archivo_global):
                menu_documentos(archivo_global)
        elif opcion == "4":
            prompt = "[+] Nueva ubicación del archivo: "
            nuevo_archivo = input("\033[1m\n" + prompt + "\033[0m").strip()
            if validar_archivo(nuevo_archivo):
                archivo_global = nuevo_archivo
                print(f"[✓] Archivo actualizado: {archivo_global}")
                pausar()
        elif opcion == "5":
            limpiar_pantalla()
            print("\n[✓] Gracias por usar Sandboxed. ¡Hasta luego!\n")
            break
        else:
            print("[!] Opción inválida")
            pausar()

    return archivo_global


def main():
    """Función principal"""
    limpiar_pantalla()
    crear_estructura_directorios()
    mostrar_banner()

    print("=" * 60)
    print("BIENVENIDO A SANDBOXED - ANÁLISIS DE MALWARE")
    print("=" * 60)
    print("")

    prompt = "[+] Ingresa la ubicación del archivo para analizar: "
    archivo = input("\033[1m" + prompt + "\033[0m").strip()

    if not archivo:
        print("\n[!] Debe ingresar una ubicación de archivo")
        sys.exit(1)

    if not validar_archivo(archivo):
        print("[!] No se puede continuar sin un archivo válido")
        sys.exit(1)

    print(f"[✓] Archivo cargado correctamente: {archivo}")
    input("\n[Presione Enter para continuar al menú principal...]")

    menu_principal(archivo)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        limpiar_pantalla()
        print("\n[!] Programa interrumpido por el usuario\n")
        sys.exit(0)
