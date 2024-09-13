#sistema para calcular promedio de notas de un alumno
print("Sistema para calcular el promedio de notas de un alumno")
nombre = input("para comenzar, cual es tu nombre: ")
matematicas = int(input(nombre + " cual es tu nota en matemáticas: "))
biologia = int(input(nombre + " cual es tu nota en biología: "))
quimica = int(input(nombre + " cual es tu nota en quimica: "))
promedio = int(matematicas + biologia + quimica) / 3
if promedio >= 10:
  print(' felicidades ' + nombre + ' "Aprobaste" con un promedio de: ',
        round(promedio), 2)
  print("sigue asi excelente en tus estudios, hasta pronto")
else:
  print("lo sentimos " + nombre, " has 'reprobado' con un promedio de: ",
        round(promedio, 2))
