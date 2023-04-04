frase = str(input('Digite sua frase: ')).strip().upper()
print('A letra "A" aparece: {} na frase'.format(frase.count('A')))
print('A primeira "A" pareceu na posicao: {}'.format(frase.find('A')+1))
print('A Ultima fez que a letra "A" apareceu na posicao: {}'.format(frase.rfind('A')+1))
