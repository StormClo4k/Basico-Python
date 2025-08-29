#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razao: '))
pa = 10
cont = 0

# minha logica foi complicada... com while cont <= 10 já funcionava
while pa != 0:
    if cont == pa:
        pa = int(input('\nQuantos termos deseja mostrar a mais? '))
        cont = 0
    else:
        print(termo,end='.')
        termo += razao
        cont += 1
print('\nFim!')
        


