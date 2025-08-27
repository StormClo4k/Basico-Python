#Exercício Python 038: Escreva um programa que leia dois números
#  inteiros e compare-os. mostrando na tela uma mensagem:

num1 = int(input('Digite o primeiro valor para comparacao: '))
num2 = int(input('Digite o segundo valor para comparacao: '))

if num1 > num2:
    print('O primeiro valor é maior')
elif num1 < num2:
    print('O segundo valor é maior') 
else:
    print('Não existe valor maior, os dois são iguais')
   