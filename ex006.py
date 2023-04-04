a = int(input('Digite o numero: '))
print('O dobro de \033[1;36m{} \033[me: \033[1m{}\n\033[mO triplo de \033[1;36m{}\033[m\033[m e: \033[1m{}\n\033[mA raiz quadrada de \033[36m{}\033[m e: \033[1m{:.2f}'.format(a, (a*2), a, (a*3), a, (a**(1/2))))
