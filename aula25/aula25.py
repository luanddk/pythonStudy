"""
Split, Join, Enumerate em Python
*Split - Dividir uma string # str
*Join - Juntar uma lista # str
*Enumerate - Enumerar elementos da lista # iteráveis
"""

string = "O brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0

for valor in lista_2:
    print(valor.strip().capitalize())

lista = ['Luiz','João','Maria']

n1, n2, n3 = lista

print(n2)