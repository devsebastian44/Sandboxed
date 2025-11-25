import os
import subprocess
import sys

def limpiar_pantalla():
    """Limpia la pantalla de forma multiplataforma"""
    os.system("clear" if os.name != "nt" else "cls")

def crear_estructura_directorios():
    """Crea la estructura de directorios necesaria"""
    directorios = ["Resultados", "Resultados/PDF"]
    for directorio in directorios:
        if not os.path.exists(directorio):
            os.makedirs(directorio)
            print(f"[✓] Directorio creado: {directorio}")

def mostrar_banner():
    """Muestra el banner de la aplicación"""
    print("")
    print("\033[91m" + r"  _________                  .______.                           .___" + "\033[0m")
    print("\033[91m" + r" /   _____/____    ____    __| _/\_ |__   _______  ___ ____   __| _/" + "\033[0m")
    print("\033[91m" + r" \_____  \\__  \  /    \  / __ |  | __ \ /  _ \  \/  // __ \ / __ | " + "\033[0m")
    print("\033[91m" + r" /        \/ __ \|   |  \/ /_/ |  | \_\ (  <_> >    <\  ___// /_/ | " + "\033[0m")
    print("\033[91m" + r"/_______  (____  /___|  /\____ |  |___  /\____/__/\_ \\___  >____ | " + "\033[0m")
    print("\033[91m" + r"        \/     \/     \/      \/      \/            \/    \/     \/ " + "\033[0m")
    print("")

def ejecutar_comando(comando, nombre_archivo, directorio="Resultados"):
    """Ejecuta un comando y guarda el resultado en un archivo"""
    try:
        dir_actual = os.getcwd()
        os.chdir(directorio)
        
        print(f"\n[*] Ejecutando: {comando}")
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True, timeout=300)
        
        salida = resultado.stdout + resultado.stderr
        
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(salida)
        
        print(f"[✓] Resultados guardados en: {directorio}/{nombre_archivo}")
        print("\n" + "="*60)
        print(salida[:2000])  # Mostrar primeros 2000 caracteres
        if len(salida) > 2000:
            print(f"\n... (output truncado, ver archivo completo en {nombre_archivo})")
        print("="*60)
        
        os.chdir(dir_actual)
        return True
        
    except subprocess.TimeoutExpired:
        print("[!] El comando excedió el tiempo límite de 5 minutos")
        os.chdir(dir_actual)
        return False
    except FileNotFoundError:
        print(f"[!] Error: Comando no encontrado. Asegúrate de que la herramienta esté instalada.")
        os.chdir(dir_actual)
        return False
    except Exception as e:
        print(f"[!] Error al ejecutar comando: {e}")
        os.chdir(dir_actual)
        return False

def validar_archivo(ruta):
    """Valida que el archivo exista"""
    if not os.path.exists(ruta):
        print(f"[!] Error: El archivo '{ruta}' no existe")
        return False
    if not os.path.isfile(ruta):
        print(f"[!] Error: '{ruta}' no es un archivo válido")
        return False
    return True

def menu_analisis_windows(archivo):
    """Menú para análisis de ejecutables Windows"""
    while True:
        print("\n" + "="*60)
        print("ANÁLISIS DE EJECUTABLES WINDOWS")
        print("="*60)
        print("[1] Propiedades estáticas")
        print("[2] Cadenas y desofuscación")
        print("[99] Volver al menú principal")
        
        opcion = input("\033[1m[+] Ingrese una opción: \033[0m").strip()
        
        if opcion == "1":
            print("\n[1] Analizar con manalyze")
            print("[2] Analizar con peframe")
            print("[99] Volver")
            sub_opcion = input("\033[1m[+] Ingrese una opción: \033[0m").strip()
            
            if sub_opcion == "1":
                ejecutar_comando(f"manalyze {archivo}", "manalyze.txt")
            elif sub_opcion == "2":
                ejecutar_comando(f"peframe {archivo}", "peframe.txt")
                
        elif opcion == "2":
            print("\n[1] Analizar con pestr")
            print("[2] Analizar con flarestrings")
            print("[3] Analizar con floss")
            print("[99] Volver")
            sub_opcion = input("\033[1m[+] Ingrese una opción: \033[0m").strip()
            
            if sub_opcion == "1":
                ejecutar_comando(f"pestr {archivo}", "pestr.txt")
            elif sub_opcion == "2":
                ejecutar_comando(f"flarestrings {archivo}", "flarestrings.txt")
            elif sub_opcion == "3":
                ejecutar_comando(f"floss {archivo}", "floss.txt")
                
        elif opcion == "99":
            break
        else:
            print("[!] Opción inválida")

def menu_analisis_linux(archivo):
    """Menú para análisis de binarios Linux"""
    while True:
        print("\n" + "="*60)
        print("ANÁLISIS DE BINARIOS LINUX")
        print("="*60)
        print("[1] Propiedades estáticas")
        print("[2] Desmontar o Descompilar")
        print("[99] Volver al menú principal")
        
        opcion = input("\033[1m[+] Ingrese una opción: \033[0m").strip()
        
        if opcion == "1":
            print("\n[1] Analizar con trid")
            print("[2] Analizar con exiftool")
            print("[99] Volver")
            sub_opcion = input("\033[1m[+] Ingrese una opción: \033[0m").strip()
            
            if sub_opcion == "1":
                ejecutar_comando(f"trid {archivo}", "trid.txt")
            elif sub_opcion == "2":
                ejecutar_comando(f"exiftool {archivo}", "exiftool.txt")
                
        elif opcion == "2":
            print("\n[1] Analizar con cutter")
            print("[99] Volver")
            sub_opcion = input("\033[1m[+] Ingrese una opción: \033[0m").strip()
            
            if sub_opcion == "1":
                print("[*] Abriendo Cutter...")
                os.system(f"cutter {archivo}")
                
        elif opcion == "99":
            break
        else:
            print("[!] Opción inválida")

def menu_documentos():
    """Menú para análisis de documentos sospechosos"""
    while True:
        print("\n" + "="*60)
        print("ANÁLISIS DE DOCUMENTOS SOSPECHOSOS")
        print("="*60)
        archivo = input("\033[1m[+] Ingresa la ubicación del archivo: \033[0m").strip()
        
        if not validar_archivo(archivo):
            continue
            
        print("\n[1] Archivos de Microsoft Office")
        print("[2] Archivos PDF")
        print("[99] Volver al menú principal")
        
        opcion = input("\033[1m[+] Ingrese una opción: \033[0m").strip()
        
        if opcion == "1":
            print("\n[1] Analizar con pcodedmp")
            print("[2] Analizar con olevba")
            print("[3] Analizar con XLMMacroDeobfuscator (Excel)")
            print("[99] Volver")
            sub_opcion = input("\033[1m[+] Ingrese una opción: \033[0m").strip()
            
            if sub_opcion == "1":
                ejecutar_comando(f"pcodedmp {archivo}", "pcodedmp.txt")
            elif sub_opcion == "2":
                ejecutar_comando(f"olevba {archivo}", "olevba.txt")
            elif sub_opcion == "3":
                ejecutar_comando(f"xlmdeobfuscator --file {archivo}", "XLMMacroDeobfuscator.txt")
                
        elif opcion == "2":
            destino = input("\033[1m[+] Directorio de salida (Enter para usar 'Resultados/PDF'): \033[0m").strip()
            if not destino:
                destino = "Resultados/PDF"
                
            print("\n[1] Analizar con pdfextract (extrae recursos binarios)")
            print("[2] Analizar con pdfresurrect")
            print("[99] Volver")
            sub_opcion = input("\033[1m[+] Ingrese una opción: \033[0m").strip()
            
            if sub_opcion == "1":
                ejecutar_comando(f"pdfextract -afjms {archivo} -d {destino}", "pdfextract.txt", "Resultados/PDF")
            elif sub_opcion == "2":
                ejecutar_comando(f"pdfresurrect {archivo}", "pdfresurrect.txt")
                
        elif opcion == "99":
            break
        else:
            print("[!] Opción inválida")

def menu_principal(archivo_inicial):
    """Menú principal de la aplicación"""
    while True:
        limpiar_pantalla()
        mostrar_banner()
        print("\n" + "="*60)
        print("MENÚ PRINCIPAL - SANDBOXED")
        print("="*60)
        print(f"Archivo actual: {archivo_inicial}")
        print("")
        print("[1] Analizar ejecutables de Windows")
        print("[2] Binarios Linux de ingeniería inversa")
        print("[3] Examinar documentos sospechosos")
        print("[4] Cambiar archivo")
        print("[5] Salir")
        
        opcion = input("\033[1m[+] Ingrese una opción: \033[0m").strip()
        
        if opcion == "":
            print("[!] Por favor ingrese una opción")
        elif opcion == "1":
            if validar_archivo(archivo_inicial):
                menu_analisis_windows(archivo_inicial)
        elif opcion == "2":
            if validar_archivo(archivo_inicial):
                menu_analisis_linux(archivo_inicial)
        elif opcion == "3":
            menu_documentos()
        elif opcion == "4":
            archivo_inicial = input("\033[1m[+] Nueva ubicación del archivo: \033[0m").strip()
            if validar_archivo(archivo_inicial):
                print(f"[✓] Archivo actualizado: {archivo_inicial}")
        elif opcion == "5":
            print("\n[✓] Saliendo de Sandboxed...")
            break
        else:
            print("[!] Opción inválida")

def main():
    """Función principal"""
    limpiar_pantalla()
    crear_estructura_directorios()
    mostrar_banner()
    
    archivo = input("\033[1m[+] Ingresa la ubicación del archivo para analizar: \033[0m").strip()
    
    if not archivo:
        print("[!] Debe ingresar una ubicación de archivo")
        sys.exit(1)
    
    if validar_archivo(archivo):
        menu_principal(archivo)
    else:
        print("[!] No se puede continuar sin un archivo válido")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Programa interrumpido por el usuario")
        sys.exit(0)