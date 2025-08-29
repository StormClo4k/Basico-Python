# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razao: '))
pa = 10
cont = termo

# minha logica foi complicada... com while cont <= 10 já funcionava
while cont in range(termo, (pa * razao)+termo):
    print(cont, end='.')
    cont += razao
