# Faça um programa que leia o número inteiro e mostre na tela seu sucessor e seu antecessor 
print('Vou dizer qual o antecessor e o sucessor do número escolhido por você!')
n = int(input('Digite um número:'))
ant = n - 1
suc = n + 1
print('O antecessor do seu número é: {} \nO sucessor do seu número é: {}'.format(ant, suc))