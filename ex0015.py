km = float(input('Quantos KM foram rodado com o carro? '))
dias = float(input('Quantos dias foram usado o carro? '))
pago = (km * 0.15) + (dias * 60)
print('Foram usados {:.0f} Dias e foram rodado {:.2f}KM, o total a se pagar e de {:.2f}R$'.format(dias, km, pago))
