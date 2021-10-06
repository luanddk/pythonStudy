"""
For / Else em python
"""

variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

comeca_com_j = False

for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print(valor)

