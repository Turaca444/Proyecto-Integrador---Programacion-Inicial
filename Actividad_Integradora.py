
#El usuario debe ingresar 5 números enteros, los cuales serán almacenados en una
#lista


print("Instituto Superior Politécnico Córdoba - Tecnicatura Superior en Innovación con Tecnologías 4.0\n")
print("Integrantes: Julio Carreño - Carolina Nis - Fernando Vexenat - Jorge Medina \n")
print("Bienvenidos a Progamación Inicial \n")

n_1=int(input("Ingrese el Primer Numero  Entero: "))
n_2=int(input("Ingrese el Segundo Numero Entero: "))
n_3=int(input("Ingrese el Tercero Numero Entero: "))
n_4=int(input("Ingrese el Cuarto Numero  Entero: "))
n_5=int(input("Ingrese el Quinto Numero  Entero: "))

lista=[n_1,n_2,n_3,n_4,n_5]
suma=0
x=0
while x<len(lista):
    suma=suma+lista[x]
    x=x+1

print("========================================================")   
print("La suma total es: ",suma)
print("========================================================")
print("Los Numeros Ingresados de la lista son: ",lista)
print("========================================================")