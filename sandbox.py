import os
import subprocess

os.system("clear")
# Definir el nombre de la carpeta
Resultados = "Resultados"

# Crear la carpeta si no existe
if not os.path.exists(Resultados):
    os.makedirs(Resultados)

# Especifica la ruta de la carpeta padre
carpeta_padre = "Resultados"

# Especifica el nombre de la nueva carpeta
carpeta_nueva = "PDF"

# Crea la ruta completa de la carpeta nueva
ruta_carpeta_nueva = os.path.join(carpeta_padre, carpeta_nueva)

# Crea la carpeta nueva dentro de la carpeta padre
if not os.path.exists(ruta_carpeta_nueva):
    os.makedirs(ruta_carpeta_nueva)


print("")

print("\033[91m" + r"  _________                  .______.                           .___" + "\033[0m")
print("\033[91m" + r" /   _____/____    ____    __| _/\_ |__   _______  ___ ____   __| _/" + "\033[0m")
print("\033[91m" + r" \_____  \\__  \  /    \  / __ |  | __ \ /  _ \  \/  // __ \ / __ | " + "\033[0m")
print("\033[91m" + r" /        \/ __ \|   |  \/ /_/ |  | \_\ (  <_> >    <\  ___// /_/ | " + "\033[0m")
print("\033[91m" + r"/_______  (____  /___|  /\____ |  |___  /\____/__/\_ \\___  >____ | " + "\033[0m")
print("\033[91m" + r"        \/     \/     \/      \/      \/            \/    \/     \/ " + "\033[0m")
print("")

pregunta = input("\033[1m\n[+] Ingresa la ubicación del archivo para analizar: \033[0m")

def menu_principal():
    while True:                                                   
        print("\n[1] Analizar ejecutables de Windows")
        print("[2] Binarios Linux de ingeniería inversa")
        print("[3] Examinar documentos sospechosos")
        print("[4] Salir")
        opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
        if opcion == "":
            print("\n[+] Por favor ingrese una opción")
        elif opcion == "1":
            menu1()
        elif opcion == "2":
            menu2()
        elif opcion == "3":
            menu3()
        elif opcion == "4":
            # Salir del programa
            break
        else:
            print("Opción inválida")



def menu1():
    while True:
        print("\n[1] Propiedades estáticas")
        print("[2] Cadenas y desofuscación")
        print("[99] Volver al menú")
        opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
        if opcion == "1":
            print("\n[1] Analizar con manalyze")
            print("[2] Analizar con peframe")
            print("[99] Volver al menú")
            opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
            if opcion == "1":
                    # Entrar a la carpeta
                    os.chdir("Resultados")
                    # Ejecutar el comando con la ubicación del archivo
                    comando = f"manalyze {pregunta}"
                    resultado = subprocess.check_output(comando, shell=True)
                    # Guardar los resultados en un archivo
                    with open("manalyze.txt", "w+") as archivo:
                        archivo.write(resultado.decode())
                        archivo.seek(0)
                        contenido = archivo.read()
                        print(contenido)
                        # Salir de la carpeta
                        os.chdir("..")  # Cambiar al directorio padre

            elif opcion == "2":
                # Entrar a la carpeta
                os.chdir("Resultados")
                # Ejecutar el comando con la ubicación del archivo
                comando = f"peframe {pregunta}"
                resultado = subprocess.check_output(comando, shell=True)
                # Guardar los resultados en un archivo
                with open("peframe.txt", "w+") as archivo:
                    archivo.write(resultado.decode())
                    archivo.seek(0)
                    contenido = archivo.read()
                    print(contenido)
                # Salir de la carpeta
                os.chdir("..")  # Cambiar al directorio padre                      

        elif opcion == "2":
            print("\n[1] Analizar con pestr")
            print("[2] Analizar con flarestrings")
            print("[3] Analizar con floss")
            print("[99] Volver al menú")
            opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
            if opcion == "1":
                # Entrar a la carpeta
                os.chdir("Resultados")
                # Ejecutar el comando con la ubicación del archivo
                comando = f"pestr {pregunta}"
                resultado = subprocess.check_output(comando, shell=True)
                # Guardar los resultados en un archivo
                with open("pestr.txt", "w+") as archivo:
                    archivo.write(resultado.decode())
                    archivo.seek(0)
                    contenido = archivo.read()
                    print(contenido)
                # Salir de la carpeta
                os.chdir("..")  # Cambiar al directorio padre   

            elif opcion == "2":
                # Entrar a la carpeta
                os.chdir("Resultados")
                # Ejecutar el comando con la ubicación del archivo
                comando = f"flarestrings {pregunta}"
                resultado = subprocess.check_output(comando, shell=True)
                # Guardar los resultados en un archivo
                with open("flarestrings.txt", "w+") as archivo:
                    archivo.write(resultado.decode())
                    archivo.seek(0)
                    contenido = archivo.read()
                    print(contenido)
                # Salir de la carpeta
                os.chdir("..")  # Cambiar al directorio padre   

            elif opcion == "3":
                # Entrar a la carpeta
                os.chdir("Resultados")
                # Ejecutar el comando con la ubicación del archivo
                comando = f"floss {pregunta}"
                resultado = subprocess.check_output(comando, shell=True)
                # Guardar los resultados en un archivo
                with open("floss.txt", "w+") as archivo:
                    archivo.write(resultado.decode())
                    archivo.seek(0)
                    contenido = archivo.read()
                    print(contenido)
                # Salir de la carpeta
                os.chdir("..")  # Cambiar al directorio padre   

        elif opcion == "99":
            # Salir del menú interno
            break

        else:
            print("Opción inválida")



def menu2():
    while True:
        print("\n[1] Propiedades estáticas")
        print("[2] Desmontar o Descompilar")
        print("[99] Volver al menú")
        opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
        if opcion == "1":
            print("\n[1] Analizar con trid")
            print("[2] Analizar con exiftool")
            print("[99] Volver al menú")
            opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
            if opcion == "1":
                    # Entrar a la carpeta
                    os.chdir("Resultados")
                    # Ejecutar el comando con la ubicación del archivo
                    comando = f"trid {pregunta}"
                    resultado = subprocess.check_output(comando, shell=True)
                    # Guardar los resultados en un archivo
                    with open("trid.txt", "w+") as archivo:
                        archivo.write(resultado.decode())
                        archivo.seek(0)
                        contenido = archivo.read()
                        print(contenido)
                    # Salir de la carpeta
                    os.chdir("..")  # Cambiar al directorio padre   

            elif opcion == "2":
                    # Entrar a la carpeta
                    os.chdir("Resultados")
                    # Ejecutar el comando con la ubicación del archivo
                    comando = f"exiftool {pregunta}"
                    resultado = subprocess.check_output(comando, shell=True)
                    # Guardar los resultados en un archivo
                    with open("exiftool.txt", "w+") as archivo:
                        archivo.write(resultado.decode())
                        archivo.seek(0)
                        contenido = archivo.read()
                        print(contenido)
                    # Salir de la carpeta
                    os.chdir("..")  # Cambiar al directorio padre   

        elif opcion == "2":
            print("\n[1] Analizar con cutter")
            print("[99] Volver al menú")
            opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
            if opcion == "1":
                os.system("cutter")

        elif opcion == "99":
            # Salir del menú interno
            break


def menu3():
    while True:
        pregunta2 = input("\033[1m\n[+] Ingresa la ubicación del archivo para analizar: \033[0m")
        print("\n[1] Archivos de Microsoft Office")
        print("[2] Archivos PDF")
        print("[99] Volver al menú")
        opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
        if opcion == "1":
            print("\n[1] Analizar con pcodedmp")
            print("[2] Analizar con olevba")
            print("[3] Analizar con XLMMacroDeobfuscator (Exel)")
            print("[99] Volver al menú")
            opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
            if opcion == "1":
                    # Entrar a la carpeta
                    os.chdir("Resultados")
                    # Ejecutar el comando con la ubicación del archivo
                    comando = f"pcodedmp {pregunta}"
                    resultado = subprocess.check_output(comando, shell=True)
                    # Guardar los resultados en un archivo
                    with open("pcodedmp.txt", "w+") as archivo:
                        archivo.write(resultado.decode())
                        archivo.seek(0)
                        contenido = archivo.read()
                        print(contenido)
                    # Salir de la carpeta
                    os.chdir("..")  # Cambiar al directorio padre   

            elif opcion == "2":
                    # Entrar a la carpeta
                    os.chdir("Resultados")
                    # Ejecutar el comando con la ubicación del archivo
                    comando = f"olevba {pregunta}"
                    resultado = subprocess.check_output(comando, shell=True)
                    # Guardar los resultados en un archivo
                    with open("olevba.txt", "w+") as archivo:
                        archivo.write(resultado.decode())
                        archivo.seek(0)
                        contenido = archivo.read()
                        print(contenido)
                    # Salir de la carpeta
                    os.chdir("..")  # Cambiar al directorio padre   

            elif opcion == "3":
                    # Entrar a la carpeta
                    os.chdir("Resultados")
                    # Ejecutar el comando con la ubicación del archivo
                    comando = f"xlmdeobfuscator --file {pregunta}"
                    resultado = subprocess.check_output(comando, shell=True)
                    # Guardar los resultados en un archivo
                    with open("XLMMacroDeobfuscator.txt", "w+") as archivo:
                        archivo.write(resultado.decode())
                        archivo.seek(0)
                        contenido = archivo.read()
                        print(contenido)
                    # Salir de la carpeta
                    os.chdir("..")  # Cambiar al directorio padre    

        elif opcion == "2":
            pregunta2 = input("\033[1m\n[+] Ingresa la ubicación del archivo para analizar: \033[0m")
            opcion2 = input("\033[1m\n[+] Ingrese una ubicación para guardar lo archivos: \033[0m")
            print("\n[1] Analizar con pdfextract (extrae recursos binarios)")
            print("[2] Analizar con pdfdecrypt (elimina el contenido cifrado)")
            print("[3] Analizar con pdfresurrect")
            print("[99] Volver al menú")
            opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
            if opcion == "1":
                    # Nos movemos a la carpeta 
                    os.chdir("Resultados/PDF")
                    # Ejecutar el comando con la ubicación del archivo
                    comando = f"pdfextract -afjms {pregunta2} -d {opcion2}"
                    resultado = subprocess.check_output(comando, shell=True)
                    # Guardar los resultados en un archivo
                    with open("pdfextract.txt", "w+") as archivo:
                        archivo.write(resultado.decode())
                        archivo.seek(0)
                        contenido = archivo.read()
                        print(contenido)

menu_principal()


