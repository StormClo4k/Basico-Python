# Exercício Python 080: Crie um programa onde o usuário possa digitar
# cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista
# ordenada na tela.

nums = list()

for cont in range(5):
    nums.append(int(input(f'Digite o valor {cont+1}: ')))

print(f'{nums}')

for i in range(5):
    print(min(nums),end=' ')
    nums.pop(nums.index(min(nums)))