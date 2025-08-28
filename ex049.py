# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um
# número que o usuário escolher, só que agora utilizando um laço for.

x = int(input('digite um valor: '))

for i in range(1, 11):
    print('{} x {} = {}'.format(x, i, x*i))
print('FIM!')
