#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem
#  e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço 
# militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = datetime.now().year # recebe somente o valor do ano atual, para o calculo da idade
idade = ano_atual - ano_nascimento

if idade < 18:
    print('Voce tera que se alistar futuramente!')
elif idade == 18:
    print('Chegou o momento de se alistar')
else:
    print('O momento de se alistar já passou')
