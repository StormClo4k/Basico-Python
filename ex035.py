# Exercício Python 35: Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não formar um triângulo.

l1 = float(input('Digite o lado 1 do triangulo: '))
l2 = float(input('Digite o lado 2 do triangulo: '))
l3 = float(input('Digite o lado 3 do triangulo: '))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('Nao é possivel formar um triangulo!!')
else:
    print('É possivel formar um triangulo!!')