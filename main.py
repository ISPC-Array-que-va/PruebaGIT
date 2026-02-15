import datos as mo

#ESCRIBIR GASTOS
for nombre in mo.nombres:
    print(nombre, end=" ")
print("\n \n")

#SUMAR GASTOS
total_gastos = 0
for i in mo.gastos:
    total_gastos = total_gastos + i
print("Total de Gastos:", total_gastos, "\n")
