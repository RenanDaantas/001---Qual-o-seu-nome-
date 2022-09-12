#ler o salário do funcionário e mostre seu novo salário com 15% de aumento
s = float(input('Digite seu salário atual e tenha uma surpresa: R$'))
a = s * 15/100
sa = s + a
print('Seu salário teve um aumento de 15% e agora você receberá R${:.2f}'.format(sa))