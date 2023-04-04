inicio = int(input('Digite o primeiro numero da PA: '))
pa = int(input('Digite a PA: '))
cont = 1
termo = inicio
while cont <= 10:
    print('{} -> '.format(inicio), end='')
    inicio += pa
    cont += 1
print('FIM!')