# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.


times_brasileirao = (
    "Atlético-MG",
    "Atlético-GO",
    "Athletico-PR",
    "Bahia",
    "Botafogo",
    "Corinthians",
    "Coritiba",
    "Chapecoense",
    "Cruzeiro",
    "Cuiabá",
    "Flamengo",
    "Fluminense",
    "Fortaleza",
    "Grêmio",
    "Internacional",
    "Juventude",
    "Palmeiras",
    "RB Bragantino",
    "São Paulo",
    "Vasco da Gama"
)

print('Os 5 primeiros colocados são: {}'.format(times_brasileirao[-5:]))
print('Os quatro ultimos são: {}'.format(times_brasileirao[0:4]))
print('Time em ordem alfabertica: {}'.format(sorted(times_brasileirao)))
print('O chapecoense está na posicao {}'.format(times_brasileirao.index('Chapecoense')+1))