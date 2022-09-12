# Faça um program que leia a altura e largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²
a = float(input('Digite a altura da sua parede:'))
l = float(input('Digite a largura da sua parede:'))
print('Baseado nesses dados, sua parede tem {:.2f} m², sendo assim são necessários {:.2f} litros de tinta.'.format((a*l), ((a*l)/2)))