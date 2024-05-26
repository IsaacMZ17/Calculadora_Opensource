from Sumar import Suma
from Restar import Resta
from Multiplicar import Multiplicacion
from Dividir import Division
from Suma_avanzada import SumaAvanzada

suma1 = Suma.sumar(3,9)

print(suma1)

resta1 = Resta.restar(13,7)

print(resta1)

multi1 = Multiplicacion.multiplicar(8,3)

print(multi1)

division1 = Division.dividir(36,3)

print(division1)

sumaA1 = SumaAvanzada.sumaAvanzada(3,1,2,4,1,5)

sumaA2 = SumaAvanzada.sumaAV([3,1,2,4,1,5])

print(sumaA1)
print(sumaA2)