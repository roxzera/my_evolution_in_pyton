frase = str(input('Digite uma palavra: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('Palindromo')
else:
    print('Nao palindromo')
