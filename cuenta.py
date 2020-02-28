# Autor: Valeria Huerta Pedregal, A01748774
# Descripcion: Leer el monto de la comida y calcular el subtotal,
# la propina, el IVA y el total a pagar

# Escribe tu programa después de esta línea.
a = float(input("Teclea el monto total de la comida: "))
sub = a
prop = a*0.13
IVA = a*0.16
t = sub + prop + IVA

print("Costo de su comida: $%.2f" % a)
print("Propina: $%.2f" % prop)
print("IVA: $%.2f" % IVA)
print("Total a pagar: $%.2f" % t)
