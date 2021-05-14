#Ejercicio 7

"""Desarrollar un algoritmo que simule una calculadora 
donde se le da como entrada dos números y el tipo de operación 
y esta devuelve el resultado."""

from mis_funciones import calculadora

operacion = input("Ingrese la operación: ")
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese un número: "))

print(calculadora(operacion,numero1, numero2))
