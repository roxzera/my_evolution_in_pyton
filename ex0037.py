num1 = int(input('Digite um numero: '))
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
num_digitado = int(input('Sua opção: '))
if num_digitado == 1:
    print('O numero {} em binario e {}'.format(num1, bin(num1)))
elif num_digitado == 2:
    print('O numero {} em Octal e {}'.format(num1, oct(num1)))
elif num_digitado == 3:
     print('O numero {} em Hexadecimal e {}'.format(num1, hex(num1)))
else:
    print('Opção invalida')