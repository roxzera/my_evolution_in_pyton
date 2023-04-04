kilo = float(input('Qual e seu peso? (KG) '))
altura = float(input('Qual seu altura? (M) '))
imc = kilo / (altura ** 2)
print('O IMC dessa pessoa e de {:.2f}'.format(imc), end=' ')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')
