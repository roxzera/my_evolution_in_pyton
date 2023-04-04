lar = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = lar * alt
tinta = area / 2
print('Sua parede de {}x{} tem area de {}m²\nE precisa de {}L de tinta para ser pintada'.format(lar, alt, area, tinta))

