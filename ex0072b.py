tublatex = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nova', 'dez', 'onze', 'doze', 'treze', 'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenova', 'vinte')
opcao = int(input('Digite um numero de 0 a 20: '))
while True:
    if opcao == len(tublatex):
        print(tublatex)
        break
