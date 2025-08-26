# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite um valor para num1: '))
num2 = int(input('Digite um valor para num2: '))
num3 = int(input('Digite um valor para num3: '))

if num1 >= num2 and num1 >= num3:
    maior = num1
    print(f'{maior} é o maior numero')
elif num2 >= num1 and num2 >= num3:
    maior = num2
    print(f'{maior} é o maior numero')
else:
    maior = num3
    print(f'{maior} é o maior numero')

if num1 <= num2 and num1 <= num3:
    menor = num1
    print(f'{menor} é o menor numero')
elif num2 <= num1 and num2 <= num3:
    menor = num2
    print(f'{menor} é o menor numero')
else:
    menor = num3
    print(f'{menor} é o menor numero')
