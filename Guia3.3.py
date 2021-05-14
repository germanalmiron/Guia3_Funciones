#Ejercicio 3

"""Desarrollar un algoritmo para calcular el área de un rectángulo."""

from mis_funciones import area

base = int(input("Ingrese la base del rectángulo en cm: "))
altura = int(input("Ingrese la altura del rectángulo en cm: "))

print("El área del rectángulo es: ", area(base, altura), "cm2")
