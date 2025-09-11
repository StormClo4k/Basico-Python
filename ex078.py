# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
nums = list()
for cont in range(5):
    nums.append(int(input(f'Digite um valor para a posicao {cont + 1}: ')))

print('O maior valor apresentado na lista foi {} e o menor foi {}'
      .format(max(nums),min(nums)))