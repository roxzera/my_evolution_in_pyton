num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
if (num1 > num2) and (num1 > num3):
    maiornumero = num1
    print('Segundo numero e maior numero digitado')
elif (num2 > num1) and (num2 > num3):
    maiornumero = num2
else:
    maiornumero = num3
if (num1 < num2) and (num1 < num3):
    menornumero = num1
elif (num2 < num1) and (num2 < num3):
    menornumero = num2
else:
    menornumero = num3
print('O menor numero foi {} e o maior foi {}'.format(menornumero, maiornumero))
