totalpessoa = 0
homens = 0
mulheres = 0
while True:
    aa = '-' * 35
    bb = 'CADASTRE UMA PESSOA'
    print(f'{aa}')
    print(f'{bb:^35}')
    print(f'{aa}')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'MmFf':
        if idade > 18:
            totalpessoa += 1
        if sexo in 'Mm':
            homens += 1
        if sexo in 'Ff' and idade < 20:
            mulheres += 1
        print(aa)
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'Nn':
            print('FIM DO PROGRAMA')
            break
        if continuar in 'Ss':
            print('', end='')
        else:
            print('Opcao invalida!')
    else:
        print('Opcao invalida')
print(f'Total de pessoa com mais de 18 anos {totalpessoa}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulher com menos de 20 anos')
