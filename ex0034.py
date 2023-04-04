salario = float(input('Digite seu salario: '))
if salario >= 1250:
    alt = salario * 0.10 + salario
    print('Seu salario foi aumentado em 10% valor: {}'.format(alt))
else:
    alt = salario * 0.15 + salario
    print('Seu salario foi aumentado em 15% valor: {}'.format(alt))
