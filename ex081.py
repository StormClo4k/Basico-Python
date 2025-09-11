# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

num = list()
s = str

while s != 'n':
    num.append(int(input('Digite um valor: ')))
    s = str(input('Digite S para continuar e N para parar: ')).lower()

print('Foran digitados {} numeros na lista!'.format(len(num)))
num.sort(reverse=True)
print('A lista de numeros em forma decrescente: {}'.format(num))
print(f'O numero 5 está na lista? {5 in num}')
