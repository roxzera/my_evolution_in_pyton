r1 = int(input('Digite o r1: '))
r2 = int(input('Digite o r2: '))
r3 = int(input('Digite o r3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triangulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    if r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima NAO PODEM FORMAR UM TRIANGULO')