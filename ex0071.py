valor = int(input('Qual o valor que voce quer sacar? '))
total = valor
cedula = 50
totalcedu = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedu += 1
    else:
        if totalcedu > 0:
            print(f'Total de notas de {totalcedu} de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedu = 0
    if total == 0:
        break
