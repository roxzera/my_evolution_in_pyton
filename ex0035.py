r1 = int(input('Digite o valor do R1: '))
r2 = int(input('Digite o valor do R2: '))
r3 = int(input('Digite o valor do R3: '))

if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Entao pode ser um triangulo')
else:
    print('Nao pode ser um triangulo')
