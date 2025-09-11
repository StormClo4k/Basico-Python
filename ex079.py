# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores 
# numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 

lista = list()
lista.append(int(input('Digite um numero inteiro')))
cont = 1

while cont < 10:
    num = int(input('Digite outro valor: '))
    if num in lista:
        cont += 1
        continue
    else:
        lista.append(num)
        cont += 1
    
print(lista)