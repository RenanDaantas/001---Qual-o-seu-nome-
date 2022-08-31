#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digite um número:'))
d = n*2
t = n*3
rq = n**(1/2)
print('O dobro do seu número é: {}\nO triplo do seu número é: {}\nA raiz quadrada do seu número é: {:.2f}'.format(d, t, rq))