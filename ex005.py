a = int(input('Digite o numero: '))
print('O numero digitado foi: \033[36m{}\n\033[mE seu sucessor e: \033[32m{}\n\033[mE seu antecessor e: \033[31m{}'.format(a, (a+1), (a-1)))
