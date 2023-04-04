soma = 0
contador = 0
num = int(input('Digite o numero: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite o numero: '))
print('O total de numeros digitado foi {}'.format(contador))
print('E a soma deles foi {}'.format(soma))
