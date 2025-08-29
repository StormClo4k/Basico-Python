# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num = count = som = 0
num = int(input('Digite o numero: [999 para parar]'))
while num != 999:
    som += num
    count += 1
    num = int(input('Digite o numero: [999 para parar]'))
print('Voce digitou {} numeros e a soma entre eles foi {}.'.format(count, som))