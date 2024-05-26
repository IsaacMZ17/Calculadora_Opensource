from Sumar import Suma
from Restar import Resta
from Multiplicar import Multiplicacion
from Dividir import Division
from Suma_avanzada import SumaAvanzada

def menu():
    print("===Hola Querido Usuario Seleccione Una Opcion===")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Suma Avanzada")
    print("6) Salir")
    print("================================================\n")

while True:
    menu()
    opc = int(input("Ingrese un numero: "))

    if opc == 1:
        a = float(input("\nIngresa el primer numero: "))
        b = float(input("\nIngresa el segundo numero: "))
        sumaRes = Suma.sumar(a,b)
        print(f"\n El resultado es: {sumaRes} \n")
    
    if opc == 2:
        a = float(input("\nIngresa el primer numero: "))
        b = float(input("\nIngresa el segundo numero: "))
        restaRes = Resta.restar(a,b)
        print(f"\n El resultado es: {restaRes} \n")

    if opc == 3:
        a = float(input("\nIngresa el primer numero: "))
        b = float(input("\nIngresa el segundo numero: "))
        multiRes = Multiplicacion.multiplicar(a,b)
        print(f"\n El resultado es: {multiRes} \n")

    if opc == 4:
        a = float(input("\nIngresa el primer numero: "))
        b = float(input("\nIngresa el segundo numero: "))
        divisionRes = Division.dividir(a,b)
        print(f"\n El resultado es: {divisionRes} \n")

    if opc == 5:
        x = 0
        b = []
        n = int(input("\nIngresa la cantidad de numeros a sumar: "))
        while n > x:
            a = float(input("Ingresa un numero: "))
            b.append(a)
            x+=1

        sumaAVRes = SumaAvanzada.sumaAvanzada(b)
        print(f"\n El resultado es: {sumaAVRes} \n")

    if opc == 6:
        print("=====Adios=====")
        break