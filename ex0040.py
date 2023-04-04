nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1+nota2) / 2
if media < 5:
    print('-'*20)
    print('Nota 1: {}'.format(nota1))
    print('Nota 2: {}'.format(nota2))
    print('Media: {}'.format(media))
    print('Status: \033[31mREPROVADO\033[m')
elif media > 7:
    print('-' * 20)
    print('Nota 1: {}'.format(nota1))
    print('Nota 2: {}'.format(nota2))
    print('Media: {}'.format(media))
    print('Status: \033[32mAprovado\033[m')
else:
    print('-'*20)
    print('Nota 1: {}'.format(nota1))
    print('Nota 2: {}'.format(nota2))
    print('Media: {}'.format(media))
    print('Status: \033[33mRECUPERAÇÃO\033[m')
