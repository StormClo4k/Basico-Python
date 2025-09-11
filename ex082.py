# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
# valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

num = list()
par = list()
impar = list()

while True:
    num.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar? S/N: ')).upper()
    if resposta == 'N':
        break

for x in num:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

print('lista principal: {}'.format(num))
print('lista de numeros pares: {}'.format(par))
print('lista de numeros impares: {}'.format(impar))
