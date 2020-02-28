# Autor: Valeria Huerta Pedregal, A01748774
# Descripcion: Calcular la distancia recorrida en 6 y 3.5 horas, y el tiempo que se requiere
# para 485km.

# Escribe tu programa después de esta línea.
v = int(input("Teclea la velocidad en km/h: "))

d = v*6
dis = v*3.5
t = 485/v

print("Velocidad del auto en km/h: ", v)
print("Distancia recorrida en 6 hrs: %.1f km" % d)
print("Distancia recorrida en 3.5 hrs: %.1f km" % dis)
print("Tiempo para recorrer 485km: %.1f hrs." % t)