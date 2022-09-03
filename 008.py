# Escreva um program que leia um valor em metros e o exiba convertido em centimetros e milímetros
x = float(input('Digite um valor em metros:'))
print('Seu valor em metros {:.0f}, convertido para cm é {:.0f} e para mm é {:.0f}'.format(x, (x*100), (x*1000)))