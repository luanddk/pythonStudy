"""
Formatanda valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO) f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

# num_1 = 10
# num_2 = 3
# divisao = num_1 / num_2
# print('{:.2f}'.format(divisao))

# num_1 = 1
# print(f'{num_1:0>10}')
#
# num_2 = 1150
# print(f'{num_2:0>10}')
#

# nome = 'Otávio'
# sobrenome = 'Miranda'
# nome_formatado = '{n:#^10} {s:#^10}'.format(n=nome, s=sobrenome)
# print(nome_formatado)

nome = 'Luan Silva'
print(nome.lower()) # tudo minusculo
print(nome.upper()) # tudo maiusculo
print(nome.title()) # somente as primeira Letras maiusculas

