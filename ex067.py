#Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
#  um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
#  quando o número solicitado for negativo.
num = int(input('Digite o valor para apresentar a tabuada: '))
cont = 1
while True:
    if num < 0:
        break
    elif cont == 10:
        cont = 1
        num = int(input('Digite o valor para apresentar a tabuada: ')) 
    else:
        cont += 1
        mult = num * cont
        print(f'{num} x {cont} = {mult}')

