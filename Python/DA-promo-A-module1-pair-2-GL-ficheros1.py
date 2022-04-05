## Pair programming pair 2, Guada, Laura - Ficheros I

# En estos ejercicios tendréis que crear dos funciones que:
# ---------------------------------- PRIMERA FUNCIÓN -----------------------
# Nos muestre en que carpeta estamos trabajando.
# Cree una carpeta que se llame "aprendiendo-ficheros". ⚠️ Tened en cuenta que si la carpeta ya existe no la podemos crear, nos devolverá un error. 
# Incluye en la función un programa que evite que nos de error si la carpeta ya existe.
# Cree otra carpeta que se llame "datos" dentro de la carpeta "aprendiendo-ficheros". En esta carpeta "datos" guardaremos el fichero "saludo.txt" 
# que os habéis descargado.
# Cambiad el directorio de trabajo a la carpeta "datos". Antes de seguir chequead que estáis trabajando en la carpeta "datos"..
# Cambiad el nombre de la carpeta creada en el punto 2 a "primera-toma-contacto"

# def donde_trabajamos():
#     import os
#     import shutil
#     origen = ("/mnt/c/Users/a/Desktop/Adalab/DA-promo-A-module-1-pairprog2-pair-2-GL/Python/saludo.txt")
#     destino = ("/mnt/c/Users/a/Desktop/Adalab/DA-promo-A-module-1-pairprog2-pair-2-GL/Python/aprendiendo-ficheros/datos/")
#     aprendiendo_ficheros = ("/mnt/c/Users/a/Desktop/Adalab/DA-promo-A-module-1-pairprog2-pair-2-GL/Python/aprendiendo-ficheros/") 
#     primera_toma_contacto = ("/mnt/c/Users/a/Desktop/Adalab/DA-promo-A-module-1-pairprog2-pair-2-GL/Python/primera-toma-contacto/")

#     os.getcwd()
#     os.chdir("/mnt/c/Users/a/Desktop/Adalab/DA-promo-A-module-1-pairprog2-pair-2-GL/Python/")
#     try:
#         os.mkdir("aprendiendo-ficheros")
#     except OSError:
#         print("La creación del directorio falló porque ya existe 'aprendiendo-ficheros'")
#     else:
#         print("Se ha creado el directorio: 'aprendiendo-ficheros'")
    
#     os.chdir("/mnt/c/Users/a/Desktop/Adalab/DA-promo-A-module-1-pairprog2-pair-2-GL/Python/aprendiendo-ficheros/")
#     os.getcwd()                                                                                                                 #quitar getcwd
#     print(os.listdir())
#     # os.mkdir("datos")                                                                                                         #otro try/except

#     # os.chdir("/mnt/c/Users/a/Desktop/Adalab/DA-promo-A-module-1-pairprog2-pair-2-GL/Python/saludo.txt")

#     # shutil.move(origen, destino)
    
#     os.chdir("/mnt/c/Users/a/Desktop/Adalab/DA-promo-A-module-1-pairprog2-pair-2-GL/Python/aprendiendo-ficheros/datos/")
#     print(os.getcwd())

#     os.chdir("/mnt/c/Users/a/Desktop/Adalab/DA-promo-A-module-1-pairprog2-pair-2-GL/Python/aprendiendo-ficheros/")
#     os.rename(aprendiendo_ficheros, primera_toma_contacto)
#     os.chdir("/mnt/c/Users/a/Desktop/Adalab/DA-promo-A-module-1-pairprog2-pair-2-GL/Python/primera-toma-contacto/datos/")       #no nos cambia el nombre de la carpeta
        # PRUEBA OS.COWN
    
    
   
# donde_trabajamos()



def leer_saludo():

    import os
    os.getcwd()

    os.chdir("/mnt/c/Users/a/Desktop/Adalab/DA-promo-A-module-1-pairprog2-pair-2-GL/Python/primera-toma-contacto/datos/")
    os.read


leer_saludo()

