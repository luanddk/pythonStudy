"""
* Enumerate - Enumerar elementos da lista # list
"""
            #0          1       2
lista = [
            ['Edu', 'João', 'Luiz'],    # 0
            ['Maria', 'Aline', 'Joana'], # 1
            ['Helena', 'Ed', 'Lu'], # 2
]

for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)