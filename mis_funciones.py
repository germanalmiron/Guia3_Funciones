def suma(num1, num2):
    """Suma dos valores"""       
    resultado = num1 + num2

    return resultado

def positivo_negativo(numero):
    """Determina si el número es positivo(devuelve true) o negativo( devuelve falso)."""
    if(numero>=0):
        return True
    else:
        return False

def area(base, altura):
    """Determina el área de un rectángulo"""
    area = base * altura
    return area

def contar_caracter(cadena, caracter):
    """Contar cuantas veces aparece el caracter en la cadena"""
    cantidad = 0
    for letra in cadena:
        if(letra == caracter):
            cantidad += 1
    return cantidad

def es_palíndromo(cadena):
    """Determina si una palabra es palindromo."""
    cadena_aux= list(cadena)
    cadena_aux.reverse()
    cadena_invertida = ""
    cadena_invertida = cadena_invertida.join(cadena_aux)
    return cadena_invertida == cadena

def sumatoria(numero):
    """Calcula h(1/n)"""
    suma = 0
    for i in range(1, numero+1):
        suma += 1/i
    return suma

def calculadora(operacion, numero1, numero2):
    "Simula la operación de una calculadora dada entre dos números"
    operacion
    if(operacion == "suma"):
        return numero1 + numero2
    elif(operacion == "resta"):
        return numero1 - numero2
    elif(operacion == "multiplicacion"):
        return numero1 * numero2
    elif(operacion == "division"):
        return numero1 / numero2
    else:
        return False

def numero_primo(numero):
    """Determina si un numero es primo (devuelve true) o no (devuelve false)."""
    for i in range(2, numero):
        if numero % i == 0:
            return False
        else:
            return True

def vocal(caracter):
    """Determina si un caracter es vocal"""
  
    if(caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u"):
        return caracter, "Es vocal"
    else:
        print("no es vocal")

def numero_mayor(numero1, numero2):
    """Determina que número es mayor"""

    if(numero1 >= numero2):
        return "El primer número es mayor"
    else:
        return "El segundo número es mayor"

def intercambiar_variable(numero1, numero2):
    "Intercambia el valor de dos variables numéricas"
    a = numero1
    b = numero2
    a, b = b, a
    return (a , b)

def aleatorio(numero1, numero2):
    "Elije un numero aleatorio entre dos numeros dados"

    from random import randint

    return randint(numero1, numero2)