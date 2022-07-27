print("=================================================================")
print("Bienvenidos!.... A continuacion, debera Ingresar 5 Numeros Enteros")
print("=================================================================", "\n")
   
num = 5
lista = []
suma = 0 
        
for i in range ( 1, 6):
    valor = int(input(f"Escriba el Numero Entero {i}: "))
    lista  = lista + [valor]
    suma = suma + i
def funcion_sumar ():
    
    print("=============================================", "\n")    
    print("La Suma de Numeros Enteros es Igual a: ", suma)

funcion_sumar()

def funcion_promedio():        
    promedio = 0
    promedio = suma / num
    print("=============================================", "\n")
    print("El Promedio es: " ,promedio)
    print("=============================================", "\n")

funcion_promedio()

        
print("La Lista contiene los Siguientes Valores: ", lista)
print("=============================================", "\n")

def funcion_maximo ():
    print("El Valor maximo ingresado es: ",max(lista))
    print("=============================================", "\n")

funcion_maximo ()
        
def funcion_minimo ():
    print ("El valor minimo ingresado es: ", min (lista))
    print("=============================================", "\n")

funcion_minimo ()
              
        