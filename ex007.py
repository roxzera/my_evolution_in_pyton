nome = str(input('Digite o nome do aluno: ')).title().strip()
nota1 = float(input('Digite a primeira nota do {}: '.format(nome)))
nota2 = float(input('Digite a segunda nota do {}: '.format(nome)))
media = (nota1+nota2) / 2
# print('Nome: {}\nNota 1: {:.1f}\nNota 2: {:.1f}\nMedia: {:.1f}'.format(nome, nota1, nota2, media))
if media >= 6:
    print('Nome: \033[4;34m{}\n\033[mNota 1: \033[1;34m{}\n\033[mNota 2: \033[1;34m{}\n\033[mMedia: \033[1;32m{}\nStatus: Aprovado'.format(nome, nota1, nota2, media))
else:
    print('Nome: \033[4;34m{}\n\033[mNota 1: \033[1;34m{}\n\033[mNota 2: \033[1:34m{}\n\033[mMedia: \033[1;31m{}\nStatus: Reprovado'.format(nome, nota1, nota2, media))
