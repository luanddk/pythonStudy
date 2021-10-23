"""
Desempacotamento de listas em python
"""
lista = ['Luiz', 'João', 'Maria',1,2,3,4,5,6,7,8,9,100]

n1, n2, n3, *outra_lista, ultimo = lista
# O * serve como resto pra frente > ou < depende de onde as variáveis sejam iniciadas ou terminadas
# ex: *outra_lista, n1, n2, n3 = lista

print(n1, n2, n3, outra_lista)