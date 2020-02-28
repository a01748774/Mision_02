# Autor: Valeria Huerta Pedregal, A01748774
# Descripcion: Calcula porcentaje de hombres, y mujeres, en el salón, y el total de alumnos.

# Escribe tu programa después de esta línea.
m = int(input("Teclea el número de mujeres inscritas: "))
h = int(input("Teclea el número de hombres inscritos: "))

t = m+h
mp = m/t*100
hp = h/t*100

print("Mujeres inscritas: ", m)
print ("Hombres inscritos: ", h)
print ("Total de inscritos: ", t)
print ("Porcentaje de mujeres: %.1f%%" % mp)
print ("Porcentjae de hombres: %.1f%%" % hp)

