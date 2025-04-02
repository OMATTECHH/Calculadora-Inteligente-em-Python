import math

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return 'Erro: Divisão por zero não é permitida'
    return x / y

def raiz(x):
    if x < 0:
        return 'Erro: não há raiz quadradas de números negativados'
    return math.sqrt(x)

def potencia(x, y):
    return x ** y

def fatorial(x):
    return math.factorial(x)
