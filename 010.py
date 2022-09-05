# Crie um program que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. considere US$=1,00 == R$3,27
rs = float(input('Informe o valor que você tem na carteira: R$'))
print('Considerando que você tem R${:.2f} é possível comprar US${:.2f}'.format(rs, (rs/3.27)))