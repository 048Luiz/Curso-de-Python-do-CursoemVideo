height = float(input('Altura da parede:'))
width = float(input('Largura da parede:'))
ink = 2 # pinta 2m² por litro de tinta. 
area = height * width
paint = area / ink 
print(f'A parede tem uma área de {area:.2f}m², e vai ser usado {paint:.2f} litros de tinta.')