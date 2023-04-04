tublatex = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nova', 'dez', 'onze', 'doze', 'treze', 'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenova', 'vinte')
opcao = int(input('Digite um numero de 0 a 20: '))
for cont in range(0, len(tublatex)):
    if opcao < 0:
        opcao = int(input('tente novamente. Digite um numero de 0 a 20: '))
    elif opcao > 20:
        opcao = int(input('tente novamente. Digite um numero de 0 a 20: '))
    else:
        if opcao == cont:
            print(tublatex[cont])
