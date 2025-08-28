# Exercício Python 51: Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

i = int(input('Digite o primeiro termo: '))
p = int(input('Digite a Razão: '))

for c in range(0, 10):
    print(i, end='.')
    i += p

print('Fim!')
