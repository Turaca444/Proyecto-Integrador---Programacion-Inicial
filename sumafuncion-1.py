

def main():
    
    print("=============================================")
    print("Bienvenidos.... Debe Ingresar Numeros Enteros")
    print("=============================================", "\n")
    num = int(input("Ingrese los Valores Solicitados --  " ))
    

    if num <=0:
        print("El Valor Ingresado es Incorreto :(  Intentar Nuevamente...")

    else: 

        lista = []
        suma = 0 
        
        for i in range ( 1, num +1):
            valor = int(input(f"Escriba el Numero Entero {i}: "))
            lista  = lista + [valor]
            suma = suma + valor
 
        print("=============================================")    
        print(f"La Suma de Numeros Enteros es Igual a: ", suma)
        print("===========================================================", "\n")
                
        print("La Lista contiene los Siguientes Valores: ", lista)
        print("===========================================================")
        
        

if  __name__== "__main__":
    main()            
        