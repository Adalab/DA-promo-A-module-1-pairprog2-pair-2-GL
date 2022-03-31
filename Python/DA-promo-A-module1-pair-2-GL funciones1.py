## Pair Programming sprint 2 - Guada y Laura - funciones I

#EJERCICIO 1
##Cread una función que reciba 2 números enteros en forma de string como entrada, y dé como resultado la suma (también en forma de string)
# Condiciones:
# Si los dos parámetros que recibe la función son strings vacíos la función nos debe devolver "0"
# Si el primer parámetro es un string vacío, la función nos devuelve el valor del segundo parámetro y viceversa.
# Probad la función para las siguientes combinaciones de "números"
    

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

arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
# resultado = [23, 64, 53, 17, 88]

def comparador(argumento1= arr1, argumento2 = arr2):
    
    zip1 = zip(arr1, arr2)
    print(list(zip1))
  
    zip1[0] == zip1[1]


    for num in arr1:
        
        if num > arr2:
            print(arr2)
        elif num == arr2:
            print(arr1)
        else:
            print(arr1)
comparador()
    

# EJERCICIO 3
# El objetivo de este ejercicio es convertir una string en un nuevo string en la que cada 
# carácter de la nueva string es "(" si ese carácter aparece sólo una vez en la string 
# original, o ")" si ese carácter aparece más de una vez en la string original. 
# Nuestro código no tiene que ser case sensitive, es decir, si hay una letra en 
# mayúscula y en minúscula cuenta como dos apariciones.
# Probad la función para los siguientes strings 

# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# "Ocvl@GamFLAFkixkS" => "((()(()()))))(()("

# def conv_str(str):
#     str =
    
#     for n in str:
#         print("")







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

n = []
s = ""
def calculadora(n,s):
    pass
    print("Resultado:", "")

calculadora(3,+)

lista1 = [11, 6, 98, 1, 2] , "*"





