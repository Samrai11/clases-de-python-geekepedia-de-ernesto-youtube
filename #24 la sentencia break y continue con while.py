#ejemplo para break
print (" while con la sentencia break \n ")
contador = 0
while contador < 10:
       contador += 1
       if contador == 5:
           break
       print ("valor actual de la variable: ", contador)
print("Fin del programa la sentencia while se ha ejecutado.")

#ejemplo para continue
print ("\n while con la sentencia continue \n ")  

contador = 0
while contador < 10:
       contador += 1
       if contador == 5:
           continue
       print ("valor actual de la variable: ", contador)
