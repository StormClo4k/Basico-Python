# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
lista = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(
    input('Digite outro valor: ')), int(input('Digite outro valor: ')))
pares = []

for i in lista:
    if i % 2 == 0:
        pares.append(i)

print('O numero 9 apareceu {} vezes na lista!'.format(lista.count(9)))
if 3 in lista:
    print('O numero 3 foi digitado na posicao {}'.format(lista.index(3)+1))
else:
    print('O numero 3 não está na lista')
print('Os numeros pares na lista são: {}'.format(pares))
