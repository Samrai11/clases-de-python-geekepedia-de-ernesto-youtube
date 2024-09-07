mensaje = "hola"
mensaje += " "
mensaje += "ernesto"
print(mensaje)
print("concatenacion")
mensaje = 'hola'
espació = " "
nombre = "ernesto"
print(mensaje + espació + nombre)
número_uno = 4
número_dos = 6
resultado = número_uno + número_dos
resultado = str(número_uno + número_dos)
print("el resultado de la suma es:" + resultado)
mensaje = "Hola Ernesto"
buscar_subcadena = mensaje.find('Ernesto')
print(buscar_subcadena)
mensaje
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)
mensaje_uno = 'hola'
mensaje_dos = 'hola'
print(mensaje_uno == mensaje_dos)
#palbaras reservadas
priNT = 5
PRint = 6
resultado = priNT + PRint
print(resultado)
#operadores aritmeticos clase 5
print("suma:")
número_uno = 5
número_dos = 4
resultado = número_uno + número_dos
print("el resultado de la suma es:" + str(resultado))
print("la resta:")
número_uno
número_dos
resultado = número_uno - número_dos
print("el resultado de la resta es:" + str(resultado))
print("la multiplicación")
número_uno
número_dos
resultado = número_uno * número_dos
print("el resultado de la multiplicación es:" + str(resultado))
print("la potenciacion en python es : **")
número_uno = 2
número_dos = 5
resultado = número_uno**número_dos
print("el resultado del exponente es:" + str(resultado))
print("la división:")
número_uno = 4
número_dos = 2
resultado = número_uno / número_dos
print("el resultado de la división es:" + str(resultado))
print("el modulo o resto es representado por el:%")
número_uno = 30
número_dos = 8
resultado = número_uno % número_dos
print("el resultado del modulo es:" + str(resultado))
print("la division entera es://")
número_uno = 4
número_dos = 2
resultado = número_uno // número_dos
print("el resultado de la división entera es:" + str(resultado))
#tipos de datos en PYTHON
número = 15
print(número, type(número))
#numeros flotantes
número_flotante = 15.5
print(número_flotante, type(número_flotante))
#tipo de dato numero complejo
número_complejo = 5 + 6j
print(número_complejo, type(número_complejo))
# tipo de dato string
nombre = "samir"
print(nombre, type(nombre))
#tipo de dato booleano
verdadero_falso = 3 == 3
print(verdadero_falso, type(verdadero_falso))

#datos desde el teclado a nuesto programa
palabra = input("introduce tu nombre: ")
num_int = int(input("introduce tu edad: "))
num_float = float(input("introduce un numero flotante: "))
num_complex = complex(input("introduce un numero comolejo: "))
print(palabra)
print(num_int)
print(num_float)
print(num_complex)
#segundo ejercicio de input desde el teclado
nombre = input("¿Cual es tu nombre?: ")
print(" hola " + nombre + " vamos a realizar una suma ")
num_uno = int(input(" por favor introduce el primer valor: "))
num_dos = int(input(" por favor introduce el segundo valor: "))
resultado = num_uno + num_dos
print(nombre + " el resultado de la suma es: " + str(resultado))
# caracteres in place
x = 5
y = x + 3
y = int(str(y) + str("x"))
