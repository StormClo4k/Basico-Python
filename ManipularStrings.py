# Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos
#  aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com
#  replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

x = 'Curso de python'

print(x[9:])
print(x[:15])
print(x.find('python'))  # indica onde a palavra comecou... ter varias palavras
print(x.count('o', 0, 10))# conta quantas vezes tem a letra O dentro do range de 0 a 10
print(len(x))  # ve o tamanho da string
print('Curso' in x)  # Existe curso em x (Retorna um valor logico)
print(x.replace('python''java'))  # Subtitui uma palavra na string por outra
print(x.upper())  # Deixa as letras maiusculas
print(x.lower())  # Deixa as letras minusculas
# Pega a string inteira, coloca as letras minusculas e deixa só a primeira letra da string em maiuscula
print(x.capitalize())
print(x.title())  # A letra inicial de todas as palavras se torna maiuscula
print(x.strip())  # Remove todos os espacos antes e depois da string
print(x.rstrip())  # Remove os espacos somente da direita
print(x.lstrip())  # Remove os espacos somente da esquerda

# Divisao

# Divide a string em varias listas, separadas pelo espaco  (Pode ser usado para contar palavras)
print(x.split())
print('-'.join(x))  # subistitui os espacos por '-' ou algum outro caractere
