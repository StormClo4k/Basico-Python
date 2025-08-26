# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite um nome completo: ')).split()
print(f'primeiro nome: {nome[0]}')
print(f'ultimo nome: {nome[-1]}')
