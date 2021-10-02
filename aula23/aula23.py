"""
Dúvidas tiradas, algumas poucas funções a mais adicionadas, quem sabe futuramente não volo aqui :D
"""


import random

lista = ['luan','lucas','leandro','jose','luciano','roseane','gustavo','paulo','pedro','josias','renato']
secreto = random.choice(lista)
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print(f'Você perdeu!! o nome era {secreto}')
        break

    letra = input('Informe uma letra: ')

    if len(letra) > 1:
        print('Informe apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print('A letra está correta uhuull!!')
    else:
        print('Poxa a letra informada está errada!!!')
        digitadas.pop()
        chances -= 1

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Você acertou o nome, parabéns !!')
        break
    else:
        print(f'A palavra está assim {secreto_temporario}')

    print(f'Você ainda tem {chances} chances')

