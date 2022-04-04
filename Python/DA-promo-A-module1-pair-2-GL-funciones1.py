## Pair Programming sprint 2 - Guada y Laura - funciones I

#EJERCICIO 1
##Cread una función que reciba 2 números enteros en forma de string como entrada, y dé como resultado la suma (también en forma de string)
# Condiciones:
# Si los dos parámetros que recibe la función son strings vacíos la función nos debe devolver "0"
# Si el primer parámetro es un string vacío, la función nos devuelve el valor del segundo parámetro y viceversa.
# Probad la función para las siguientes combinaciones de "números"

#Opción 1:
# def funcion1(string1, string2):
#     if string1 == " " and string2 == " ":
#         print("0")
#     elif string1 == " ":
#         print(string2)
#     elif string2 == " ":
#         print(string1)
#     else:
#         num1 = int(string1)
#         num2 = int(string2)
#         total_string = num1 + num2
#         print("La suma de", string1, "+", string2, "es", str(total_string)) 
# #para solucionar lo de los espacios tal vez se soluciona con lo de los 
# funcion1(,)

# a = 0
# b = 0
# def suma( a,b ):
#     print(a + b)
# print("Para completar la suma incluye dos números separados por una coma ej: (3,2)")
# if a == "":
#     a = 0
# elif b == "":
#     b = 0

# suma(2,3)

# "4",  "5" --> "9"
# "34", "5" --> "39"
# "", "" --> "0"
# "2", "" --> "2"
# "-5", "3" --> "-2"



# EJERCICIO 2
# El objetivo es comparar cada par de enteros de 2 listas, y devolver una nueva lista de números grandes.
# Probad la función para las siguientes listas: 
# 💡 Pista 💡 En Python existe el método zip.

#Opción Alicia:

arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
# # resultado = [23, 64, 53, 17, 88]

# opcion 1
# def comparador(argumento1= arr1, argumento2 = arr2):

#     num_mayores = []
#     zip1 = zip(arr1, arr2)
#     print(zip1)
    
#     for a,b in zip1[0][0]:
#         if a < b:
#             num_mayores[b]
#         elif b > a:
#             num_mayores[a]
#         else:
#             num_mayores[b]

# comparador()


    # zip1[0] == zip1[1]

    # for num in arr1:
    #     if num > arr2:
    #         print(arr2)
    #     elif num == arr2:
    #         print(arr1)
    #     else:
    #         print(arr1)

# comparador()
#opción 2: con lo que pasó Guada al slack
# arr1 = [13, 64, 15, 17, 88]
# arr2 = [23, 14, 53, 17, 80]
# arr_total = [(13, 23), (64, 14), (15, 53), (17, 17), (88, 80)]
# type(arr1)
# # zip1 = list(zip(arr1, arr2))
# # print(zip1)

# def comparador(argumento1= arr1, argumento2 = arr2):

#     lista_num_mayores = []
    
#     for i in arr_total[0]: 
                  
#         for j in arr_total[0]:              #13,23
#             a,b = arr_total[0][0], arr_total[0][1]

#             print(j)
                                
#             if a <= b:
#                 lista_num_mayores[b] 
#             else:
#                 lista_num_mayores[a]
#         lista_num_mayores = lista_num_mayores.append()

# comparador()



#opción 3
# arr1 = [13, 64, 15, 17, 88]
# arr2 = [23, 14, 53, 17, 80]
# type(arr1)
# zip1 = list(zip(arr1, arr2))
# print(zip1)

# def comparador(argumento1= arr1, argumento2 = arr2):

#     lista_num_mayores = []
    
#     for i in zip1[0]: 
                  
#         for j in zip1:              #13,23
#             print(j)
                               
#             if i <= j:
#                 lista_num_mayores[j] 
#             else:
#                 lista_num_mayores[i]
#         lista_num_mayores = lista_num_mayores.append()

# comparador()

arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
# resultado = [23, 64, 53, 17, 88]


def comparador (arr1, arr2):
    z = 0     #variable que representa la posición de la lista
    arr3=[]     #Para meter las cosas en la lista
    for i in range(len(arr1)):
        z=z+1      #repetición de bucle
        if arr1[(z-1)] <= arr2[(z-1)]:
            arr3.append(arr2[(z-1)])
        else:  
            arr3.append(arr1[(z-1)])
    print(arr3)                  

comparador(arr1, arr2)



# EJERCICIO 3
# El objetivo de este ejercicio es convertir una string en un nuevo string en la que cada carácter de la nueva string es "(" si ese carácter aparece sólo una vez en la string 
# original, o ")" si ese carácter aparece más de una vez en la string original. Nuestro código no tiene que ser case sensitive, es decir, si hay una letra en 
# mayúscula y en minúscula cuenta como dos apariciones. Probad la función para los siguientes strings 

# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# "Ocvl@GamFLAFkixkS" => "((()(()()))))(()("



# def conv_str(str):
palabra = ["din"]
palabra_out = []

for i in palabra[0]:
    print("esta es la i: ", i)
        # veces = palabra.count(i)
        # if veces == 1:
        #     print("(")
        #     # palab_out = "(" .join() añadir elementos?
        # elif veces != 1:
        #     print(")")
    
        # print(veces)
    # palab_out =     


# conv_str("din") 
#ver solución Anne (min 40). https://us02web.zoom.us/rec/play/5jwk2UArIqrgsPe5K4y9VrOO-pzm-I9a2e8JR5craZWA_Lgw9e7P9csjY8xFxDBKKkD3u_2u9_9bEDbr.mpetH1FwJEtKXiRZ?continueMode=true&_x_zm_rtaid=eBzLX_O7RwG_AMoR4UZbYw.1648802053437.4e8f769f2ff9e35d5dbc811300261ac6&_x_zm_rhtaid=439 
#averiguar qué parte le estamos pidiendo y no existe (list out of range)






######################## BONUS
# EJERCICIO 4
# A Pete le gusta hacer pasteles. Tiene algunas recetas e ingredientes. Desgraciadamente, no se le dan bien las matemáticas. 
# ¿Puedes ayudarle a averiguar cuántas tartas puede hacer teniendo en cuenta sus recetas?
# Escribid una funció, que tome la receta (diccionario) y los ingredientes disponibles 
# (también un diccionario) y devuelva el número máximo de pasteles que Pete puede hornear (entero). 
# Para simplificar, no hay unidades para las cantidades (por ejemplo, 1 libra de harina o 200 g de azúcar son simplemente 1 o 200). 
# Los ingredientes que no están presentes en los diccionarios, pueden ser considerados como 0.
# Probad con los siguientes diccionarios: 

# RECETA {'flour': 500, 'sugar': 200, 'eggs': 1}, 
# INGREDIENTES {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}

# RESULTADO: 2 
# ----------

# RECETA {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
# INGREDIENTES {'sugar': 500, 'flour': 2000, 'milk': 2000}

# RESULTADO 0







# EJERCICIO 5
# Escribid una función que va a ser una calculadora. La lista recibirá dos parámetros, un a lista de números y un string con la operación que queremos hacer (puede ser "*", "+")
# Probad con los siguientes inputs

# lista1 = [11, 6, 98, 1, 2] , "*"
# RESULTADO 12936

# -----------------------------------
# lista2 = [23,34, 56, 11, 90] , "+"
# RESULTADO 214

# -----------------------------------
# lista3 = [23, 4,109 , 94, 77] , "-"
# RESULTADO 'Lo siento, necesito que me pases una operación valida.'

# n = []
# s = ""
# def calculadora(n,s):
#     pass
#     print("Resultado:", "")

# calculadora(3,+)

# lista1 = [11, 6, 98, 1, 2] , "*"





