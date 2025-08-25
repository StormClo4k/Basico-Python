#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Digite um nome completo: '))

print('Nome com todas as letras maiusculas: {}'.format(nome.upper()))
print('nome tem {} letras! '.format(len(nome.replace(' ', ''))))
nome = nome.split()
print('O seu primeiro nome tem {} letras'.format(len(nome[0])))