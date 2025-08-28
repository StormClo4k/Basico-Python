# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

x = int(input('Digite um numero inteiro: '))
primo = 0

for i in range(1, x+1):
    if (x % i == 0):
        print('\033[32m{}\033[32m'.format(i), end=' ')
        primo += 1
    else:
        print('\033[31m{}\033[31m'.format(i), end=' ')

print('\nO numero {} foi divisivel {} vezes'.format(x, primo))

if primo == 2:
    print('\n\033[32mO numero é primo!\033[32m')
else:
    print('\033[31mO numero não é primo!\033[31m')
