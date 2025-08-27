# Exercício Python 37: Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher qual será a base de conversão: 1 para
#  binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numero inteiro: '))
condicao = int(input('Digite: 1 para conversão binária, 2 para conversão octal e 3 para conversão hexadecimal: '))


if condicao == 1:
    print(f'A conversao de {num} para binario é: {bin(num)[2:]}')
elif condicao == 2:
    print(f'A conversao de {num} para octal é: {oct(num)[2:]}')
elif condicao == 3:
    print(f'A conversao de {num} para hexadecimal é: {hex(num)[2:]}')
else:
    print('A condicao informada é invalida')