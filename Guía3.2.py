#Ejercicio 2

"""Desarrollar un algoritmo que determine si un número es positivo o negativo."""

from mis_funciones import positivo_negativo

numero = int(input("Ingrese un número: "))

if(positivo_negativo(numero)):
    print("El número es positivo")
else:
    print("El número es negativo")
