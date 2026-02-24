import datos as mo

import colorama
from colorama import Fore
from colorama import Style

#ESCRIBIR GASTOS
for nombre in mo.nombres:
    print(nombre, end=" ")
print("\n \n")

#SUMAR GASTOS
total_gastos = 0
for i in mo.gastos:
    total_gastos = total_gastos + i
print(Fore.RED + Style.BRIGHT + "Total de Gastos:" + Style.RESET_ALL, total_gastos)

#SUMAR ingresos
total_ingresos = 0
for i in mo.ingresos:
    total_ingresos = total_ingresos + i
print(Fore.GREEN + "Total de Ingresos:"+ Style.RESET_ALL, total_ingresos)

#Saldo
Saldo = total_ingresos - total_gastos

print(Fore.BLUE + Style.BRIGHT + "Saldo = "+ Style.RESET_ALL, Saldo, "\n")

print("Desarrollador: Iván Bürcher")