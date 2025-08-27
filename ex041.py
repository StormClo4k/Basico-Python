# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import datetime

now = datetime.now().year
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = now - ano_nascimento

print('O atleta tem {} anos de idade!'.format(idade) )

if idade > 25:
    print('Categoria: MASTER')
elif idade > 19 and idade >= 25:
    print('Categoria: SÊNIOR')
elif idade > 14 and idade >= 19:
    print('Categoria: JÚNIOR')
elif idade > 9 and idade >= 14:
    print('Categoria: INFANTIL')
else:
    print('Categoria: MIRIM')
    