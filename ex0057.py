sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('\033[31mOpção invalida! tente novamente\033[m')
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
if sexo == 'M':
    print('Seu sexo e masculino ')
elif sexo == 'F':
    print('Seu sexo e feminino')
