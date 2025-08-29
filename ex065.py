#  Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
#  No final da execução, mostre a média entre todos os valores e qual foi o maior e
#  o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
#  a digitar valores.

# CODIGO TEM QUE SER REFATORADO... EXISTE SOLUCAO MAIS FACIL

num = cont = maio = media = meno = 0
continuar = ''
while continuar != 'N':
    num = int(input('Digite um numero: '))
    if cont == 0:
        cont += 1
        maio = num
        meno = num
        media += num
    elif num > maio:
        maio = num
        cont += 1
        media += num
    elif num < meno:
        meno = num
        cont += 1
        media += num
    else:
        cont += 1
        media += num
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()

media = media / cont
print('Voce digitou {} valores\nMAIOR = {}\nMENOR = {}\nMEDIA = {}'.format(
    cont, maio, meno, media))
