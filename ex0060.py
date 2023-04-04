from math import factorial
numero = int(input('Digite um numero: '))
f = numero + 1
l = factorial(numero)
'''for c in range(numero, 0, -1):  # com for
    conta = c * resul
    resul = conta
print('Conta com for {}'.format(resul))'''
while f > 1:
    f -= 1
    print(f, 'x' if f > 1 else '=', end=' ')
print(l)
