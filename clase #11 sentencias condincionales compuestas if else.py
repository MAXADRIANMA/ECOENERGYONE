print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, ¿Cúal es tu nombre?: ")

matematicas = float (input(nombre + ", ¿Cúal es tu calificación en matematicas?: "))
biologia = float (input(nombre + ", ¿Cúal es tu calificación en biología?: "))
quimica = float (input(nombre + ", ¿Cúal es tu calificación de química?: "))

promedio = (matematicas + biologia + quimica)/3

if promedio >= 6:
    print("Felicidades " + nombre +", aprobaste con un promedio de: ", promedio)
    print("Felicidades " + nombre +", aprobaste con un promedio de: ", round(promedio, 2))
else:
    print("Rayos " + nombre + ", reprobaste con un promedio de: ", promedio)
    print("Rayos " + nombre + ", reprobaste con un promedio de: ", round(promedio, 2))
print("Bye " + nombre + ", gracias por utilizar el programa")

















