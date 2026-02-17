import datos as mo

#ESCRIBIR GASTOS
for nombre in mo.nombres:
    print(nombre, end=" - ")
print("\n \n")

#SUMAR GASTOS
total_gastos = 0
for i in mo.gastos:
    total_gastos = total_gastos + i
print("Total de Gastos:", total_gastos, "\n")

#SUMAR ingresos
total_ingresos = 0
for i in mo.ingresos:
    total_ingresos = total_ingresos + i
print("Total de Ingresos:", total_ingresos, "\n")

#Saldo
Saldo = total_ingresos - total_gastos

print("Saldo = ", Saldo, "\n")


print("desarrollador: Iván Bürcher")